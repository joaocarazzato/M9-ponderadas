import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from confluent_kafka import Consumer
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

def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def main():
  config = read_config()
  topic = "topic_0"
      # sets the consumer group ID and offset  
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"

  # creates a new consumer and subscribes to your topic
  consumer = Consumer(config)
  consumer.subscribe([topic])
  try:
    while True:
      # consumer polls the topic and prints any incoming messages
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        try:
            sensor_params = {
                'sensor': key, 
                'valor': value
                }
            database.insert_one(sensor_params)
        except:
          print("Ocorreu um erro ao registrar o dado ao banco de dados.")
        print(f"Consumed message from topic {topic}: key = {key} value = {value}")
  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()

main()
