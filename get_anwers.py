#coding:utf8

import requests
from time import sleep


HOST = "localhost"
PORT = 31366

pos_sentence = "I love AXA"
neg_sentence = "I hate AXA"

while True:
    r = requests.get("http://{}:{}/analyze?sentence=".format(HOST, PORT) + pos_sentence)
    print(r.text)
    sleep(1)
    r = requests.get("http://{}:{}/analyze?sentence=".format(HOST, PORT) + neg_sentence)
    print(r.text)
    sleep(1)
