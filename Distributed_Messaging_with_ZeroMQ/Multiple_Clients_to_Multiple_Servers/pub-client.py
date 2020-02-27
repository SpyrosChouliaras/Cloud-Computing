import sys,zmq

try:
	port1 = sys.argv[1]
	port2 = sys.argv[2]
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	print(port1)
	print(port2)
	print("Collecting updates from weather servers...")
	socket.connect("tcp://193.61.36.160:%s" % port1)
	socket.connect("tcp://193.61.36.160:%s" % port2)
	topicfilter ="10001"
	socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
	total_value=0

	for update_nbr in range(1,5):
		data = socket.recv()
		topic, messagedata,port = data.split()
		total_value += int(messagedata)
		print("Topic: '%s', message: '%d' on port '%d' " %(topic,int(messagedata),int(port)))
		print("Average message data value for topic '%s' was '%dF'" % (topicfilter, total_value/ update_nbr))

except KeyboardInterrupt:
	context.destroy()
	socket.close()


