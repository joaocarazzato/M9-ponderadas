import paho.mqtt.client as mqtt
import time
import csv
from dotenv import load_dotenv
import os

load_dotenv()


file_path = "./sensor_data/data.csv"
columns_data = {"sensor": [], "data": []}
update_time = 1
x = 0

server = os.getenv('SERVER')
port = int(os.getenv('PORT'))
keepalive = int(os.getenv('KEEPALIVE'))
username = os.getenv('USERNAME_MQTT')
pw = os.getenv('PW_MQTT')


def get_sensor_data(file_path):
  # Initialize an empty list for each column name
    with open(file_path, newline='') as csvfile:
    # Cria um leitor CSV
        reader = csv.reader(csvfile)
        # Itera sobre as linhas do arquivo
        next(reader)
        for row in reader:
            # Extrai o nome do sensor e seu dado
            columns_data["sensor"].append(row[0])  # Supondo que a primeira coluna seja o nome do sensor
            columns_data["data"].append(row[1])         # Supondo que a segunda coluna seja o dado do sensor
            
    print(columns_data)
    return columns_data

def publish_broker():
    # Configuração do cliente
    client = mqtt.Client("py-publisher")
    client.username_pw_set(username, pw)
    client.tls_set()
    # Conecte ao broker
    client.connect(server, port, keepalive)
    # Loop para publicar mensagens continuamente
    try:
        while True:
            sensor_name, sensor_data = show_sensor_data()
            if sensor_data == "nan":
                client.disconnect()
                print("Publicação encerrada.")
                quit()
            message = "" + sensor_data
            client.publish(f"sensor/{sensor_name}", message)
            print(f"Publicado: {message} no tópico: 'sensor/{sensor_name}'")
            time.sleep(float(update_time))
    except KeyboardInterrupt:
        print("Publicação encerrada.")

    client.disconnect()


def show_sensor_data():
    global x
    if x < len(columns_data["sensor"]):
        sensor_name = columns_data["sensor"][x]
        sensor_data = columns_data["data"][x]
        x += 1
        return sensor_name, sensor_data
        
    else:
        print("Publicação de dados finalizada.")
        return "nan", "nan"

def main():
    get_sensor_data(file_path)
    publish_broker()

if __name__ == "__main__":
    main()