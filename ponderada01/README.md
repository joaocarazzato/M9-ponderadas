# Simulação de Dispositivo MQTT
O objetivo desse repositório, é simular como ocorre a transferência de dados de sensores através de um sistema MQTT. O sensor usado para exemplo é o sensor de radiação solar HOBOnet RXW-LIB-900.



https://github.com/joaocarazzato/M9-ponderadas/assets/99187756/289adc38-95c7-46f2-93e2-1e07b45ca2a3



## Instalação e Requisitos
Para instalação, é necessário ter o Python e o [Eclipse Mosquitto](https://mosquitto.org)(para simular um Broker) instalados. Após isso, precisamos baixar a biblioteca Paho MQTT do python com o seguinte comando:
```
pip install paho-mqtt
```

Após isso, temos que utilizar 3 terminais para rodar todas as necessidades do nosso projeto:
1. Broker(Mosquitto)
2. Subscriber(py-subscriber.py)
3. Publisher(py-publisher.py)

Primeiro rodamos o mosquitto:
```
mosquitto -c pasta_do_repositorio/mosquitto.conf
```
em seguida o subscriber em outro terminal:
```
python3 py-subscriber.py
```
e por fim, o publisher em outro terminal:
```
python3 py-publisher.py
```

Assim, as mensagens começarão a ser transmitidas pelo publisher, sendo inscritas no tópico `sensor/radiation_1`(nesse caso, o nome atribuído ao sensor). Podemos alterar os dados enviados no arquivo .csv encontrado dentro da pasta **sensor_data**, podendo ser adicionados novos servidores e dados.
