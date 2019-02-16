import sys
import numpy as np
def myFunction():
    print("this is my function")


# print(sys.modules.keys())
a=np.array([4,2,3,1])
remove_ixs=np.where(a>1)[0]
b=np.delete(a,remove_ixs)
print(b)
