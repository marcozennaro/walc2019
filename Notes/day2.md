__OTG microusb__
<br/>https://www.amazon.com/UGREEN-Adapter-Samsung-Controller-Android/dp/B00N9S9Z0G

__Configuración Raspberry Pi__
```
sudo raspi-config
```

__Instalación Mosquitto Raspberry Pi__
```
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
```

__Iniciar servicio Mosquitto__
```
sudo systemctl enable mosquitto.service
```

__Verbose Mosquitto__
```
mosquitto -v
```

__Suscriber__
```
mosquitto_sub -d -t iot_8
```

__Publisher__
```
mosquitto_pub -d -t iot_8 -m "10"
```

__Configurar WiFi en la Raspberry Pi__
```
sudo raspi-config
option 2 Network Options
```

__Reiniciar La RPi__
```
sudo init 6
```

__Mostrar la IP__
```
ip a
```