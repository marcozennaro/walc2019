__TTN Broker__
<br/>Server:us-west.thethings.network
<br/>port: 1883

__Security__
<br/>username: nombre_app
<br/>password: access key

__MV Ubuntu__
<br/>usuario: iot
<br/>clave: iot

__Instalación paquetes NodeRed MV Ubuntu__
<br/>sudo apt install git

__INTRODUCCION JSON__
<br/>http://json.org/

__FUNCION (PARSE JSON)__
<br/>var temp = msg.payload["temperature"]
<br/>msg.payload = temp;
<br/>return msg;


__GATEWAYS LoRa__
<br/>https://www.thethingsnetwork.org/docs/gateways/thethingsindoor/
<br/>https://pycom.io/product/pygate/
<br/>https://store.rakwireless.com/products/rak2245-pi-hat?variant=26653392535652

<br/>https://keptenkurk.wordpress.com/2018/09/21/plotting-ttn-gateways-on-a-map/

__TTN MAPPER__
<br/>https://play.google.com/store/apps/details?id=org.ttnmapper.phonesurveyor&hl=es_GT
<br/>https://ttnmapper.org


__InfluxDB__
<br/>sudo service influxdb start
<br/>sudo service grafana-server start