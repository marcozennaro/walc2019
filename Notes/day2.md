
_OTG microusb_
___
https://www.amazon.com/UGREEN-Adapter-Samsung-Controller-Android/dp/B00N9S9Z0G

__Comandos__<br />
clear<br />
sudo raspi-config
<br /><br />
__INSTALACIÓN MOSQUITTO RASPBERRY PI__<br />
sudo apt update<br />
sudo apt install -y mosquitto mosquitto-clients
<br /><br />
__INICIAR SERVICIO MOSQUITTO__<br />
sudo systemctl enable mosquitto.service
<br /><br />
__VERBOSE MOSQUITTO__<br />
mosquitto -v
<br /><br />
__SUSCRIBER__<br />
mosquitto_sub -d -t iot_8
<br /><br />
__PUBLISHER__<br />
mosquitto_pub -d -t iot_8 -m "10"
<br /><br />
__Configurar WiFi en la Raspberry Pi__<br />
sudo raspi-config<br />
option 2 NETWORK OPTIONS
<br /><br />
__REINICIAR LA RPi__<br />
sudo init 6
<br /><br />
__DESCUBRIR LA IP__<br />
ip a