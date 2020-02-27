import zmq
import pprint
context = zmq.Context()

results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://193.61.36.160:5558")

collecter_data = {}
data = {}
asum=0
for x in range(10):
	result = results_receiver.recv_json()
	print(result['num'])
	if result['consumer'] in collecter_data:
		collecter_data[result['consumer']][0] = collecter_data[result['consumer']][0] + 1
		collecter_data[result['consumer']][1] = collecter_data[result['consumer']][1] + result['num']
	else:
		collecter_data[result['consumer']] = [1,result['num']]

pprint.pprint(collecter_data)

