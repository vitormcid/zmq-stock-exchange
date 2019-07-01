import sys
import zmq
import os

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)


companies_list = ["google", "apple", "amazon", "ICBC",  "Bank of America", 
			  "Royal Dutch Shell", "Wells Fargo", "ExxonMobil", "Citigroup",
			  "Toyota Motor", "microsoft", "Alphabet",   "Volkswagen Group",
			  "Chevron", "HSBC Holdings", "intel", "Comcast",    "Softbank",
			  "RBC", "Nestle"]

companies_to_sub = []

def subscribe_to_companies():
	for i in companies_to_sub:
		sock.setsockopt(zmq.SUBSCRIBE, i)	


subscribe_to_companies()
sock.connect("tcp://127.0.0.1:5680")
message_buffer = []

company = ""

while company != "exit\n":
	print (companies_list)
	print ("digite a empresa que voce deseja se inscrever")
	company = sys.stdin.readline()
	if company != "exit\n":
		companies_to_sub.append(company.rstrip('\n'))



while True:	   
	print ("teste")
	message_buffer.append(sock.recv())
	print ("teste")
	if len(message_buffer) >= len(companies_to_sub):
		# os.system('clear')
		print ("teste")
		for i in message_buffer:
			print i
		message_buffer = []

