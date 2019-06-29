import zmq
import os

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)


companies_to_sub = ["google", "apple", "amazon", "ICBC",  "Bank of America", 
			  "Royal Dutch Shell", "Wells Fargo", "ExxonMobil", "Citigroup",
			  "Toyota Motor", "microsoft", "Alphabet",   "Volkswagen Group",
			  "Chevron", "HSBC Holdings", "intel", "Comcast",    "Softbank",
			  "RBC", "Nestle"]

def subscribe_to_companies():
	for i in companies_to_sub:
		sock.setsockopt(zmq.SUBSCRIBE, i)	


subscribe_to_companies()
sock.connect("tcp://127.0.0.1:5680")
message_buffer = []

while True:	
    message_buffer.append(sock.recv())
    if len(message_buffer) >= len(companies_to_sub):
		os.system('clear')
		for i in message_buffer:
			print i
		message_buffer = []

