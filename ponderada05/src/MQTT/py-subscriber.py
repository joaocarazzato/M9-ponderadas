import paho.mqtt.client as mqtt
import requests

server = "7ca9b605946f4f25a3fbaf9f87e13625.s1.eu.hivemq.cloud"
port = 8883
keepalive = 60
username = "admin"
pw = "Admin123"

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    try:
        requests.post(f'http://localhost:5000/gravar_dado', params= {'sensor': message.topic, 'valor': message.payload.decode()})
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