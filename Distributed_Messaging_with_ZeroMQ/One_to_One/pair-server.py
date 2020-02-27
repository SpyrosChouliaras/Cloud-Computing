import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.PAIR)

socket.setsockopt(zmq.LINGER,0)

socket.bind("tcp://193.61.36.160:5555")

while True:
	socket.send_string("Server message to Client")
	msg = socket.recv()
	print(msg)
	time.sleep(1)
