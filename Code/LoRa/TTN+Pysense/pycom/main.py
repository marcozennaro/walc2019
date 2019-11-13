# ---------------------------------------------------------------------
# Lopy program to acquire data from pysense board
# and send them to TTN via LoraWan
# Ver 1.0 2019/03/25
# ---------------------------------------------------------------------
#
import machine
import pycom
from pysense import Pysense
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
import micropython
import machine
from network import LoRa
import socket
import struct
import binascii
import ubinascii
import sys
import time
import utime

# ----------------- Pysense sensor initialization
py = Pysense()
# The MPL3115A2 returns height in meters.
# Mode may also be set to PRESSURE, returning a value in Pascals
# Sensor Data limits:
# Altitude: 20-bit: –698 to 11775 m
# Temperature: 12-bit: -40 C to 85 C
SensPress = MPL3115A2(py,mode=ALTITUDE)

# ----------------- activating LoRa
print("activating LoRa")
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

dev_addr = struct.unpack(">l", binascii.unhexlify('2602108C'))[0]
nwk_swkey = binascii.unhexlify('4F1651F280226B0B3898E5F46B4B96B7')
app_swkey = binascii.unhexlify('45C82343FA18FEDDC4D9BDF5E1C698A2')

for channel in range(0, 72):
    lora.remove_channel(channel)


for i in range(0,7):
    lora.add_channel(i, frequency=(903900000  + 200000 * i), dr_min=0, dr_max=3)


# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# remove all the non-default channels
for i in range(4, 16):
    lora.remove_channel(i)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
time.sleep(5)



print("start loop")
while True:
     # ----------------- get data from MPL3115A2 sensor
    temperature = SensPress.temperature()
    altitude = SensPress.altitude()
    # DEBUG
    print("Temperature: {} Degrees  Altitude: {}".format(temperature, altitude))
    #
    # ---------------------------------------------
    # PREPARE LORA MSG
    # ---------------------------------------------
    # The measurements to be sent on TTN must have one decimal place after the comma
    #
    # table of msg fields:
    # n | Id            | example   | lim. values           | lim rapr.    | n. bytes | start pos.
    # 1 | temperature   | 21.9      | -40.0 C to 85.0 C     | 0 .. 1250    | 2        | 0
    # 2 | altitude      | 118.4     | –698.0 to 11775.0 m   | 0 .. 124730  | 3        | 2
    # n. bytes payload: 5
    # Index range of array: 0..4
    msgLora = bytearray(5)
    # ----------------- initialize lora msg
    # set rapresentation of temperature value
    pos=0
    value = int( ( (temperature + 40.0 ) * 10.0 ) + 0.5 )
    msgLora[pos+0] = (value >> 8) & 0xff
    msgLora[pos+1] = (value) & 0xff

    # set rapresentation of altitude value
    pos=2
    value = int( ( (altitude + 698.0 ) * 10.0) + 0.5 )
    msgLora[pos+0] = (value >> 16) & 0xff
    msgLora[pos+1] = (value >> 8) & 0xff
    msgLora[pos+2] = (value) & 0xff
    #
    # ----------------- END OF LORA MSG PREPARATION
    # DEBUG
    print(msgLora)
    # ----------------- send msgLora to TTN via LoraWan
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
    s.send(msgLora)                     # send data to TTN
    #
    print("----------------------------[END MSG TX LORA]")
    #
    # ---------------------------------------------
    #
    time.sleep(15)                      # wait 15 seconds
