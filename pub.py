from __future__ import division
import zmq
import time
from random import randint



# ZeroMQ Context
context = zmq.Context()

stock_list = {"google":50, "apple":50, "amazon":50}

def update_stock_price():
	for i in stock_list:
		# the stock price can vary by up to 10%
		rand_percentage = randint(-100,100)/1000
		old_price = stock_list[i]
		stock_list[i] = old_price + old_price*rand_percentage 

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5680")

id = 0

while True:
    time.sleep(1)
    id, now = id+1, time.ctime()

    for i in stock_list:
    	update_stock_price()
    	message = "{company}-{stock_price}".format(company= i, stock_price = stock_list[i])
    	sock.send(message)
    	id += 1


    # Message [prefix][message]
    # message = "1-Update! >> #{id} >> {time}".format(id=id, time=now)
    # sock.send(message)

    # # Message [prefix][message]
    # message = "2-hello >> #{id} >> {time}".format(id=id, time=now) 
    # sock.send(message)

    

