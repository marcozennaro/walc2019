__Configuración Nodo TTN Broker__
<br/>**Server:** us-west.thethings.network
<br/>**port:** 1883

__Security__
<br/>**username:** nombre_app
<br/>**password:** access key

__Credenciales MV Ubuntu__
<br/>**usuario:** iot
<br/>**clave:** iot

__Prerequisito para instalación de paquetes NodeRed MV Ubuntu__
```
sudo apt install git
```

__Introducción JSON__
<br/>http://json.org/

__Función (parse JSON)__
```
var temp = msg.payload["temperature"]
msg.payload = temp;
return msg;
```

__Gateways LoRa__
<br/>https://www.thethingsnetwork.org/docs/gateways/thethingsindoor/
<br/>https://pycom.io/product/pygate/
<br/>https://store.rakwireless.com/products/rak2245-pi-hat?variant=26653392535652

__TTN Mapper__
<br/>https://play.google.com/store/apps/details?id=org.ttnmapper.phonesurveyor&hl=es_GT
<br/>https://ttnmapper.org

__NodeRed TTN Mapper__
<br/>https://keptenkurk.wordpress.com/2018/09/21/plotting-ttn-gateways-on-a-map/

__InfluxDB__
```
sudo service influxdb start
sudo service grafana-server start
```