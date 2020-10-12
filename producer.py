import paho.mqtt.client as mqtt
import random
import json

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost', 1883)

temperatura = random.uniform(17, 30)
print(temperatura)

mensagem = {
    'Cliente': 'Inatel',
    'temperatura': temperatura
}

mqtt_client.publish('in242', json.dumps(mensagem))
