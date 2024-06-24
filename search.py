import numpy as np
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

#use where to create searchingconditions
x = np.where(np1 == 4)
print(np1)
print(x)
print(x[0])

y = np.where(np1 % 2 == 0)
print(y[0])