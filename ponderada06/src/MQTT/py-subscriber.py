import paho.mqtt.client as mqtt
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
port = int(os.getenv('PORT'))
keepalive = int(os.getenv('KEEPALIVE'))
username = os.getenv('USERNAME_MQTT')
pw = os.getenv('PW_MQTT')
mongo_user= os.getenv('MONGO_USER')
mongo_pass= os.getenv('MONGO_PASS')


uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.4b4rfa4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    database = client["sensor_data"]["sensor_data"]
except Exception as e:
    print(e)

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    try:
        sensor_params = {
            'sensor': message.topic, 
            'valor': message.payload.decode()
            }
        database.insert_one(sensor_params)
    except:
        print("Ocorreu um erro ao registrar o dado ao banco de dados.")
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com código de resultado "+str(rc))
    # Inscreva no tópico aqui, ou se perder a conexão e se reconectar, então as
    # subscrições serão renovadas.
    client.subscribe("sensor/#")

# Configuração do cliente
client = mqtt.Client("python_subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, pw)
client.tls_set()
# Conecte ao broker
client.connect(server, port, keepalive)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()