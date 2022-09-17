import paho.mqtt.client as mqtt   # Import MQTT Library
import time
import json
from datetime import datetime


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    data = json.loads(message.payload.decode("utf-8"))
    print(data)
    print("Just printed JSON")
    print( "DateTime = ", data["timestamp"], type(data["timestamp"]) )
    dt = datetime.strptime(data["timestamp"], '%Y-%m-%dT%H:%M:%SZ')
    print ((dt), type(dt))
    readings = data["readings"]
    print( "Pressure = ", readings["pressure"], type(readings["pressure"]) )
    print( "Humidity = ", readings["humidity"], type(readings["humidity"]) )
    print( "Temperature = ", readings["temperature"], type(readings["temperature"]) )
    
    
    
import paho.mqtt.client as mqtt #import the client1
broker_address="localhost" 
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","enviro/kitchen")
client.subscribe("enviro/kitchen")
client.on_message=on_message        #attach function to callback


client.loop_start()    #start the loop

