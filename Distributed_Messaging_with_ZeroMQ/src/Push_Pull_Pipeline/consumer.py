import time
import zmq
import random

def heavyTask(i):
	return i

def consumer():
	consumer_id = random.randrange(1,10005)
	print("I am consumer #%s" % (consumer_id))
	context = zmq.Context()
	consumer_receiver = context.socket(zmq.PULL)
	consumer_receiver.connect("tcp://193.61.36.160:5557")
	consumer_sender = context.socket(zmq.PUSH)
	consumer_sender.connect("tcp://193.61.36.160:5558")
	while True:
		work = consumer_receiver.recv_json()
		data = work['num']
		result= {'consumer':consumer_id, 'num': heavyTask(data)}
		print(result)
		consumer_sender.send_json(result)
consumer()
