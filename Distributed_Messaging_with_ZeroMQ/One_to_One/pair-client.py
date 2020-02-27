import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.PAIR)

socket.setsockopt(zmq.LINGER,0)

socket.connect("tcp://193.61.36.160:5555")

count = 0

while count<10:
	msg = socket.recv()
	print(msg.decode())
	socket.send_string("Hello from Client")
	socket.send_string("This is a client message to server")
	print("Counter:  ",count)
	count+=1
	time.sleep(1)

context.destroy()
socket.close()

