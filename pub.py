from __future__ import division
import zmq
import time
from random import randint



# ZeroMQ Context
context = zmq.Context()

stock_list = {"google":50, "apple":50, "amazon":50, "ICBC":50,    "Bank of America": 50, 
			  "Royal Dutch Shell":50, "Wells Fargo":50, "ExxonMobil":50, "Citigroup":50,
			  "Toyota Motor": 50, "microsoft":50, "Alphabet":50,  "Volkswagen Group":50,
			  "Chevron":50, "HSBC Holdings": 50,"intel":50, "Comcast":50, "Softbank":50,
			  "RBC":50, "Nestle": 50,
			 }

def update_stock_price():
	for i in stock_list:
		# the stock price can vary by up to 10%
		rand_percentage = randint(-100,100)/1000
		old_price = stock_list[i]
		stock_list[i] = round(old_price + old_price*rand_percentage,3)

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5680")

while True:
    time.sleep(1)
    time.ctime()
    for i in stock_list:
    	update_stock_price()
    	message = "{company}: ${stock_price}".format(company= i, stock_price = stock_list[i])
    	sock.send(message)
    	


   

