# Trabalho final IN242
#Prof.: Lúcio

import paho.mqtt.client as mqtt
import json

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.190.79.7', 1883)

print(' Numero de pessoas')
pessoas = int(input('Digite a quantidade de pessoas: '))
print('\a') # => sinal sonoro , pelo menos comigo funcionou '-'
print(pessoas)

mensagem = {
    'Cliente': 'Inatel',
    'pessoas': pessoas
}

mqtt_client.publish('in242', json.dumps(mensagem))





