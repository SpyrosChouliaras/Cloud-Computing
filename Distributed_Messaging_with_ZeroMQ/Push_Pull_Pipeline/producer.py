import time
import zmq
import random

def producer():
	mysum = 0
	context = zmq.Context()
	zmq_socket = context.socket(zmq.PUSH)
	zmq_socket.bind("tcp://193.61.36.160:5557")
	for num in range(10):
		val = random.randint(1,5)
		work_message = {'num':val}
		zmq_socket.send_json(work_message)
		print(work_message)
		mysum = mysum + val
		time.sleep(1)
	return mysum

print(producer())
