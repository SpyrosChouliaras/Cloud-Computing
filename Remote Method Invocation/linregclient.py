import Pyro4

import random

x,y=[1,2,3],[3,5,7]
res = Pyro4.Proxy("PYRONAME:models")
print(res.estimate_coef(x,y))
