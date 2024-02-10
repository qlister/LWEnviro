from datetime import datetime
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
#    print("Connected flags ",str(flags),"result code ",str(rc))
    pass

myInky = LWInky.LWdisplay()
myDB = SQLiteDB.db()
#myDB.create_blank()


#broker_address="192.168.86.244" 
broker_address="localhost" 
client = mqtt.Client("P1", True) #create new instance
client.username_pw_set("mos-serv", "L1qu0r1ce")
client.connect(broker_address) #connect to broker
client.subscribe("enviro/kitchen")
client.subscribe("enviro/outdoor")
client.on_message=on_message        #attach function to callback
client.on_connect = on_connect

client.loop_start()    #start the loop

then = datetime.now()
then = datetime.now().minute
#print ( 'then = ' + str(then) )

while True:
    
    now = datetime.now().minute
#    print ( 'now = ' + str(now) )
    if now != then:
        then = now
#        myInky.draw( )
        
    while not msgQ.empty():   # This will sequentially read out queued messages
        data = msgQ.get()
        
        m = data['model']
        print( 'Model = ' + m )
        
        if m == 'urban':
            myDB.add_urban_data( data )
        elif m == 'indoor':
            myDB.add_kitchen_data( data )
        else:
            print("Remote MQTT device not recognised")

    time.sleep( 0.5 )    # check the queue twice a second (approx)



