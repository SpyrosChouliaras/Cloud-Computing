import zmq
import time

try:
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.setsockopt(zmq.LINGER,0)
	socket.bind("tcp://193.61.36.160:5556")
	while True:
		message=socket.recv()
		print("Received request: ",message)
		time.sleep(1)
		socket.send_string("Hi from Server")
except KeyboardInterrupt:
	context.destroy
	socket.close()


