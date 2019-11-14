from network import LoRa
import struct
import binascii
import socket


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

from time import sleep
data = [0]

while 1:
    s.setblocking(True)
    s.send(bytes(data))
    s.setblocking(False)
    s.recv(64)
    data[0] = data[0] + 1
    if data[0] > 255:
        data[0] = 0
    print(data)
    sleep(10)
