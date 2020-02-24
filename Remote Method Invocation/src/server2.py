import Pyro4
@Pyro4.expose
class Server1(object):
	def myCount(self, alist, key):
		print("Someone accessed Server2.count")
		count = 0
		for i in alist:
			if i == key:count+=1
		return(count,"2")		#1 for load balancer 1

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Server1)
ns.register("Server2", uri)  	# Register as Server1
print("Server2 is live!")
daemon.requestLoop()

