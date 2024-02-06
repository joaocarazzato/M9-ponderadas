import paho.mqtt.client as mqtt
import time
from random import randint

# Configuração do cliente
client = mqtt.Client("py-publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para publicar mensagens continuamente
try:
    while True:
        message = "Sensor de radiação: " + str(randint(0, 1280)) + " W/m2"
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()