
# Simulador MQTT com Banco de Dados e Dashboard
O objetivo deste repositório é criar um Simulador MQTT com um cluster em nuvem(HiveMQ), armazenando dados localmente através de um banco de dados em SQLite3 e a exibição desses dados utilizando um dashboard criado com o Metabase onde há persistência de dados.


https://github.com/joaocarazzato/M9-ponderadas/assets/99187756/3547c2e4-2729-492d-bd47-437b5e61259e


## Instalação
Para instalação, é necessário ter o Python instalado. Após isso, precisamos baixar a biblioteca Paho MQTT e Flask do python com o seguinte comando:
```
pip install paho-mqtt flask
```

E então, temos que alterar a linhas de **username**, **pw** e **server** para os dados e informações de acesso do cluster a ser utilizado.

```
server = "my-server-id.s1.eu.hivemq.cloud"
port = 8883
keepalive = 60
username = "my-username"
pw = "my-password"
```

Após isso, temos que utilizar 3 terminais para rodar todas as necessidades iniciais do nosso projeto:
1. API(api/flask_api.py)
2. Subscriber(MQTT/py-subscriber.py)
3. Publisher(MQTT/py-publisher.py)

Primeiro, é necessário rodar a API em flask:
```
python3 api/flask_api.py
```

E então, rodamos o subscriber:
```
python3 MQTT/py-subscriber.py
```
e por fim, o publisher em outro terminal:
```
python3 MQTT/py-publisher.py
```

Assim, as mensagens começarão a ser transmitidas pelo publisher utilizando o cluster do HiveMQ, sendo inscritas no tópico `sensor/radiation_1`(nesse caso, o nome atribuído ao sensor) e enviado ao banco de dados através da nossa API. Podemos alterar os dados enviados no arquivo .csv encontrado dentro da pasta **sensor_data**, podendo ser adicionados novos servidores e dados.
Após isso, precisamos executar nosso dashboard com o metabase utilizando o [Docker](https://www.docker.com/get-started/):

(Importante ressaltar que é necessário criar uma pasta chamada **metabase-data** dentro da pasta **src** para que a persistência de dados ocorra)

Para rodar a aplicação, devemos executar o seguinte comando:
```
docker compose up
```

Assim, nosso dashboard já estará rodando no porta 3001 do nosso [localhost](http://localhost:3001), pronto para a exibição e visualização dos dados do nosso banco de dados.

(Caso você precise adicionar o banco de dados, selecione a opção de banco **SQLite** e digite o caminho da pasta: **"/app/sqlite-db/database.db"**.)
