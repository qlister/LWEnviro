
import paho.mqtt.client as mqtt   # Import MQTT Library
import time
import json
from queue import Queue
import SQLiteDB
import LWInky

msgQ = Queue()

def on_message(cl, userdata, message):
    #    print("message received " ,str(message.payload.decode("utf-8")))
    msgQ.put(json.loads(message.payload.decode("utf-8")))

    #import matplotlib.pyplot as plt
    #plt.plot([1, 2, 3], [1, 4, 9])
    #plt.savefig('foo.png')

def on_connect(client, userdata, flags, rc):
    print("Connected flags ",str(flags),"result code ",str(rc))


myInky = LWInky.LWdisplay()
myDB = SQLiteDB.db()
#myDB.create_blank()


#broker_address="192.168.86.244" 
broker_address="localhost" 
client = mqtt.Client("P1", True) #create new instance
client.username_pw_set("mos-serv", "L1qu0r1ce")
client.connect(broker_address) #connect to broker
client.subscribe("enviro/kitchen")
client.on_message=on_message        #attach function to callback
client.on_connect = on_connect

client.loop_start()    #start the loop


while True:
    while not msgQ.empty():   # This will sequentially read out queued messages
        data = msgQ.get()
#        print( str(readings) )      
        myDB.add_kitchen_data( data )
        
        myInky.draw( data )

    time.sleep(0.5)



