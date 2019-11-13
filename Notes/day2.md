
_OTG microusb_
___
https://www.amazon.com/UGREEN-Adapter-Samsung-Controller-Android/dp/B00N9S9Z0G

_Comandos_
___
clear
sudo raspi-config

_INSTALACIÓN MOSQUITTO RASPBERRY PI_
___
sudo apt update
sudo apt install -y mosquitto mosquitto-clients


_INICIAR SERVICIO MOSQUITTO_
___
sudo systemctl enable mosquitto.service

_VERBOSE MOSQUITTO_
___
mosquitto -v

_SUSCRIBER_
___
mosquitto_sub -d -t iot_8

_PUBLISHER_
___
mosquitto_pub -d -t iot_8 -m "10"

_Configurar WiFi en la Raspberry Pi_
___
sudo raspi-config

option 2 NETWORK OPTIONS

_REINICIAR LA RPi_
___
sudo init 6

_DESCUBRIR LA IP_
___
ip a