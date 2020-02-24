import Pyro4
import random

alist = []
prev = 0

for i in range(100):
	current=random.randint(1,10) + prev
	alist.append(current)
	prev=current

print(alist)

key = int(input("Give a key to search: "))

res = Pyro4.Proxy("PYRONAME:search")

print(res.LinearSearch(alist,key))
