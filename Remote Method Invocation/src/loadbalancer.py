import Pyro4
@Pyro4.expose
class LoadBalancer(object):
	c=0 # counter is set to zero
	def callServer(self,name,alist,key): # A method to call servers
		res = Pyro4.Proxy(name)	# pass the name of the server
		result = res.myCount(alist,key) # pass the list and the key
		return result # return the results
	def roundRobin(self,alist,key): # implement the round robin
		if LoadBalancer.c==0: # Access the class variable
			result = LoadBalancer.callServer(self,"PYRONAME:Server1",alist,key)
			LoadBalancer.c=1
			return result
		else:
			result = LoadBalancer.callServer(self,"PYRONAME:Server2",alist,key)
			LoadBalancer.c=0
			return result
		print("Load balancer used: ", LoadBalancer.c)
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(LoadBalancer)
ns.register("LoadBalancer", uri)
print("Load balancer is live!")
daemon.requestLoop()

