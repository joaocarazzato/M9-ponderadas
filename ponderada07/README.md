
# Simulador MQTT com fila Apache Kafka
O objetivo deste repositório é criar um Simulador MQTT com um cluster em nuvem(HiveMQ), passando por uma fila em Apacha Kafka e armazenando dados em um banco de dados NoSQL MongoDB, disponibilizando a exibição desses dados utilizando um dashboard criado com o Metabase onde há persistência de dados.


https://github.com/joaocarazzato/M9-ponderadas/assets/99187756/90880563-c595-4186-83b0-b9f4f9efa8f1


## Instalação
Para instalação, é necessário ter o Python instalado. Após isso, precisamos baixar a biblioteca Paho MQTT, Flask, Confluent Kafka, requests e pymongo do python com o seguinte comando:
```
pip install paho-mqtt flask confluent_kafka requests pymongo
```

E então, temos que criar um .env dentro da pasta **MQTT** e definir os seguintes parametros:

```
SERVER = "my-server-id.s1.eu.hivemq.cloud"
PORT = 8883
KEEPALIVE = 60
USERNAME_MQTT = "my-username"
PW_MQTT = "my-password"
MONGO_USER = "mongouser"
MONGO_PASS = "mongopassword"
```

Após isso, temos que utilizar 3 terminais para rodar todas as necessidades iniciais do nosso projeto:
1. Subscriber(MQTT/py-kafka-subscriber.py)
2. Publisher(MQTT/py-publisher.py)

Primeiro, é necessário rodar o nosso subscriber:
```
python3 MQTT/py-kafka-subscriber.py
```
e por fim, o publisher em outro terminal:
```
python3 MQTT/py-publisher.py
```
(Na prática, não é necessário uma ordem para rodar ambos por conta do uso do Apache Kafka)

Assim, as mensagens começarão a ser transmitidas pelo publisher utilizando o cluster do HiveMQ, sendo inscritas no tópico `sensor/radiation_1`(nesse caso, o nome atribuído ao sensor), em seguida passando por nossa fila Kafka do Confluent e então sendo enviado ao banco de dados através da nossa API. Podemos alterar os dados enviados no arquivo .csv encontrado dentro da pasta **sensor_data**, podendo ser adicionados novos servidores e dados.

Após isso, precisamos executar nosso dashboard com o metabase utilizando o [Docker](https://www.docker.com/get-started/):

(Importante ressaltar que é necessário criar uma pasta chamada **metabase-data** dentro da pasta **src** para que a persistência de dados ocorra)

Para rodar a aplicação, devemos executar o seguinte comando:
```
docker compose up
```

Assim, nosso dashboard já estará rodando no porta 3001 do nosso [localhost](http://localhost:3001), pronto para a exibição e visualização dos dados do nosso banco de dados.

(Caso você precise adicionar o banco de dados, selecione a opção de banco **MongoDB** e digite a linha de conexão do seu banco do MongoDB.)
