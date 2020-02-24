import Pyro4

@Pyro4.expose

class Search(object):
	def LinearSearch(self, alist, key):
		for i in alist:
			if i == key:
				return True
		return False

daemon = Pyro4.Daemon()

ns = Pyro4.locateNS()

uri = daemon.register(Search)

ns.register("search",uri)
print("Ready.!")

daemon.requestLoop()


