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

while True:
    message= sock.recv()
    os.system('clear')	
    print(message)

