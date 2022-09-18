
import paho.mqtt.client as mqtt   # Import MQTT Library
import time
import json
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont
from inky.mock import InkyMockImpression
#import paho.mqtt.client as mqtt #import the client1
from queue import Queue

msgQ = Queue()

def on_message(cl, userdata, message):
#    print("message received " ,str(message.payload.decode("utf-8")))
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)
    data = json.loads(message.payload.decode("utf-8"))
    
    msgQ.put(data)
    
#    print(data)
#    print("Just printed JSON")
#    print( "DateTime = ", data["timestamp"], type(data["timestamp"]) )
#    dt = datetime.strptime(data["timestamp"], '%Y-%m-%dT%H:%M:%SZ')
#    print ((dt), type(dt))
#    readings = data["readings"]
#    print( "Pressure = ", readings["pressure"], type(readings["pressure"]) )
#    print( "Humidity = ", readings["humidity"], type(readings["humidity"]) )
#    print( "Temperature = ", readings["temperature"], type(readings["temperature"]) )
 

    #import matplotlib.pyplot as plt
    #plt.plot([1, 2, 3], [1, 4, 9])
    #plt.savefig('foo.png')


inky = InkyMockImpression()
font = ImageFont.truetype('truetype/dejavu/DejaVuSans.ttf', 40, encoding="unic")

#canvas = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
#draw = ImageDraw.Draw(canvas)
#unicode_text = 'Temp = %04.1f' % readings["temperature"]
#draw.text((5,5), unicode_text, 'black', font) # This paste the unicode_text=u"SMILE WORLD"
#text_width, text_height = font.getsize(unicode_text)
#unicode_text = 'Time = %s' % data["timestamp"]
#draw.text((5,40), unicode_text, 'black', font) # This paste the unicode_text=u"SMILE WORLD"

#image.paste(plot_image, (0, 0))
#saturation = 0
#inky.set_image(canvas, saturation=saturation)
#inky.show()

broker_address="localhost" 
#print("creating new instance")
client = mqtt.Client("P1") #create new instance
#print("connecting to broker")
client.username_pw_set("mos_serv", "L1qu0r1ce")
client.connect(broker_address) #connect to broker
#print("Subscribing to topic","enviro/kitchen")
client.subscribe("enviro/kitchen")
client.on_message=on_message        #attach function to callback

client.loop_start()    #start the loop

while True:
    while not msgQ.empty():   # This will sequentially read out queued messages
        data = msgQ.get()
        dt = datetime.strptime(data["timestamp"], '%Y-%m-%dT%H:%M:%SZ')
        readings = data["readings"]
#        print( "Pressure = ", readings["pressure"], type(readings["pressure"]) )
#        print( "Humidity = ", readings["humidity"], type(readings["humidity"]) )
#        print( "Temperature = ", readings["temperature"], type(readings["temperature"]) )
        canvas = Image.new("RGB", (inky.width, inky.height), (255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        unicode_text = 'Temp = %04.1f\N{DEGREE SIGN}C' % readings["temperature"]
        draw.text((5,80), unicode_text, 'black', font)
        text_width, text_height = font.getsize(unicode_text)
        unicode_text = dt.strftime('%a, %d, %b %Y')
        draw.text((5,5), unicode_text, 'black', font)

#        image.paste(plot_image, (0, 0))
        saturation = 0
        inky.set_image(canvas, saturation=saturation)
        inky.show()

    time.sleep(0.5)



