
# Simulação de Dispositivo MQTT utilizando HiveMQ.
O objetivo desse repositório, é simular como ocorre a transferência de dados de sensores através de um sistema MQTT utilizando um cluster do HiveMQ. O sensor usado para exemplo é o sensor de radiação solar HOBOnet RXW-LIB-900.


https://github.com/joaocarazzato/M9-ponderadas/assets/99187756/ba893b5d-1ee9-4540-8b9f-b9334829fa47


## Instalação e Requisitos
Para instalação, é necessário ter o Python instalado. Após isso, precisamos baixar a biblioteca Paho MQTT do python com o seguinte comando:
```
pip install paho-mqtt
```

E então, temos que alterar a linhas de **username**, **pw** e **server** para os dados e informações de acesso do cluster a ser utilizado.

```
server = "my-server-id.s1.eu.hivemq.cloud"
port = 8883
keepalive = 60
username = "my-username"
pw = "my-password"
```

Após isso, temos que utilizar 2 terminais para rodar todas as necessidades do nosso projeto:
1. Subscriber(py-subscriber.py)
2. Publisher(py-publisher.py)

Primeiro, rodamos o subscriber:
```
python3 py-subscriber.py
```
e por fim, o publisher em outro terminal:
```
python3 py-publisher.py
```

Assim, as mensagens começarão a ser transmitidas pelo publisher utilizando o cluster do HiveMQ, sendo inscritas no tópico `sensor/radiation_1`(nesse caso, o nome atribuído ao sensor). Podemos alterar os dados enviados no arquivo .csv encontrado dentro da pasta **sensor_data**, podendo ser adicionados novos servidores e dados.
Também podemos realizar testes para verificar sua funcionalidade com o arquivo python dentro da pasta **tests**.
