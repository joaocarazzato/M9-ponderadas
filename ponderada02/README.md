# Testes de Dispositivo MQTT
O objetivo desse repositório, é simular como ocorre a transferência de dados de sensores através de um sistema MQTT e realizar testes para verificar seu funcionamento utilizando o pytest.


https://github.com/joaocarazzato/M9-ponderadas/assets/99187756/2ac78bc5-d868-4f14-acd6-d9408243d1b5


## Instalação e Requisitos
Para instalação, é necessário ter o Python e o [Eclipse Mosquitto](https://mosquitto.org)(para simular um Broker) instalados. Após isso, precisamos baixar a biblioteca Paho MQTT e pytest do python com o seguinte comando:
```
pip install paho-mqtt pytest
```

Após isso, temos que utilizar 3 terminais para rodar todas as necessidades do nosso projeto:
1. Broker(Mosquitto)
2. testes de subscriber(py-subscriber.py)

Primeiro rodamos o mosquitto:
```
mosquitto -c pasta_do_repositorio/mosquitto.conf
```
em seguida os testes em outro terminal, dentro da pasta **tests**:
```
python3 -m pytest
```
Dessa forma, 3 testes serão rodados: um para verificar o recebimento, outro para verificar alterações na mensagem enviada e a recebida e por último, para verificar o QoS das mensagens.


Podemos alterar os testes a serem executados editando o arquivo **test_subscriber.py** para nossas necessidades.
