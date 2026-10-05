# Approach 1

# import package1.test1 as t
# import package1.pack2.module9 as q
#
# t.display()
# obj1=q.A()
# obj1.justname('raghu')


# Approach 2

from package1.test1 import display
from package1.pack2.module9 import *

display()
obj1=A()
obj1.justname('raghu')






