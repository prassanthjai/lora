import paho.mqtt.client as mqtt
import base64
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("application/3/node/+/rx")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    d = json.loads(msg.payload)
    print("data : " + base64.b64decode(d['data']))
    #print("device : " + base64.b64decode(d['deviceName']))

client = mqtt.Client()
client.username_pw_set("loraroot", "root")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.201", 1883, 60)

client.loop_forever()
