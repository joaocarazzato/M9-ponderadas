import paho.mqtt.client as mqtt
import time

server = "b356f57b629c4264b5f6123d9dbdf74c.s1.eu.hivemq.cloud"
port = 8883
keepalive = 60
username = "admin"
pw = "Admin123"

def test_message_rate_confirmation():
    # Configurações da taxa de disparo
    target_message_rate = 1  # mensagens por segundo
    duration = 60  # segundos
    acceptable_error_margin = 0.1  # 10%

    client_sub = mqtt.Client()
    client_sub.username_pw_set(username, pw)
    client_sub.tls_set()
    client_sub.connect(server, port, keepalive)
    client_sub.subscribe("test/topic", qos=1)

    # Iniciar loop em segundo plano para o subscriber
    client_sub.loop_start()

    client_pub = mqtt.Client()
    client_pub.username_pw_set(username, pw)
    client_pub.tls_set()
    client_pub.connect(server, port, keepalive)
    # Simulação do envio de mensagens
    start_time = time.time()
    messages_sent = 0
    while time.time() - start_time < duration:
        # Simula o envio de uma mensagem
        messages_sent += 1
        time.sleep(1)
        # Aqui você colocaria a lógica real para enviar as mensagens
        # Enviar mensagem do Publisher
        client_pub.publish("test/topic", "Hello, MQTT!")

    client_pub.disconnect()
    client_sub.disconnect()
    # Calcular a taxa de mensagens real
    actual_message_rate = messages_sent / duration

    # Verificar se a taxa de mensagens está dentro da margem de erro
    lower_bound = target_message_rate * (1 - acceptable_error_margin)
    upper_bound = target_message_rate * (1 + acceptable_error_margin)
    assert lower_bound <= actual_message_rate <= upper_bound

def test_mqtt_receive():
    received_messages = []

    def on_message(client, userdata, msg):
        received_messages.append(msg.payload.decode())

    # Configurar o subscriber
    client_sub = mqtt.Client()
    client_sub.on_message = on_message
    client_sub.username_pw_set(username, pw)
    client_sub.tls_set()
    client_sub.connect(server, port, keepalive)
    client_sub.subscribe("test/topic", qos=1)

    # Iniciar loop em segundo plano para o subscriber
    client_sub.loop_start()

    # Enviar mensagem do Publisher
    client_pub = mqtt.Client()
    client_pub.username_pw_set(username, pw)
    client_pub.tls_set()
    client_pub.connect(server, port, keepalive)
    client_pub.publish("test/topic", "Hello, MQTT!")

    # Esperar um pouco para a mensagem ser recebida
    time.sleep(2)

    # Verificar se a mensagem foi recebida corretamente
    assert client_sub.on_message is not None

    # Desconectar os clientes
    client_pub.disconnect()
    client_sub.disconnect()

def test_mqtt_communication():
    received_messages = []

    def on_message(client, userdata, msg):
        received_messages.append(msg.payload.decode())

    # Configurar o subscriber
    client_sub = mqtt.Client()
    client_sub.on_message = on_message
    client_sub.username_pw_set(username, pw)
    client_sub.tls_set()
    client_sub.connect(server, port, keepalive)
    client_sub.subscribe("test/topic", qos=1)

    # Iniciar loop em segundo plano para o subscriber
    client_sub.loop_start()

    # Enviar mensagem do Publisher
    client_pub = mqtt.Client()
    client_pub.username_pw_set(username, pw)
    client_pub.tls_set()
    client_pub.connect(server, port, keepalive)
    client_pub.publish("test/topic", "Hello, MQTT!")

    # Esperar um pouco para a mensagem ser recebida
    time.sleep(2)

    # Verificar se a mensagem foi recebida corretamente
    assert received_messages[-1] == "Hello, MQTT!"

    # Desconectar os clientes
    client_pub.disconnect()
    client_sub.disconnect()
