import zmq
import os

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE, "google")
sock.setsockopt(zmq.SUBSCRIBE, "amazon")
sock.setsockopt(zmq.SUBSCRIBE, "apple")
sock.connect("tcp://127.0.0.1:5680")

sub_count = 3
message_buffer = []

while True:	
    message_buffer.append(sock.recv())
    if len(message_buffer) >= sub_count:
		os.system('clear')
		for i in message_buffer:
			print i
		message_buffer = []

