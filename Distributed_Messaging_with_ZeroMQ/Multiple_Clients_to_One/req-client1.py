import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.setsockopt(zmq.LINGER,0)

socket.connect("tcp://193.61.36.160:5556")

for request in range(1,10):
	print("Sending request Client 1", request, " .... ")
	socket.send_string("Hello from client 1")
	message = socket.recv()
	print("Received reply ",request, "[", message, "]")

socket.close()
context.destroy()


