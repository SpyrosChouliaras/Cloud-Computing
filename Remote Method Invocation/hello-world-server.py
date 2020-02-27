import Pyro4

@Pyro4.expose

class HelloWorldMaker(object):
	def get_message(self,name):
		print("CALL: get message method") #Log point
		return "Hello world {0}\n"\
			"This message is coming from the sever".format(name)

	def sum_of_2(self, a, b):
		print("CALL: sum_of_2 method")
		return int(a) + int(b)


daemon = Pyro4.Daemon()

uri = daemon.register(HelloWorldMaker)

print("Ready. Object uri =",uri)
daemon.requestLoop()
