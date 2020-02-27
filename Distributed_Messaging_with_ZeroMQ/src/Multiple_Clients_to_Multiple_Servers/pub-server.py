import zmq
import random
import sys
import time

try:
	port = sys.argv[1]
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.bind("tcp://193.61.36.160:%s" % port)
	while True:
		topic = random.randrange(9999,10005)
		messagedata = random.randrange(1,215) -80
		print("%d %d"% (topic,messagedata))
		socket.send_string("%d %d %d"% (topic,messagedata,int(port)))
		time.sleep(1)

except KeyboardInterrupt:
	context.destrory()
	socket.close()

