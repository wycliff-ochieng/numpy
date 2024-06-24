import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

np2 = np.array([[1,2,3,4], [5,6,7,8]])
print(np2)
print(np2.shape)

#reshaping
np3 = np1.reshape(3,4)
print(np3)
print(np3.shape)

np4 = np1.reshape(2,3,2)
print(np4)
print(np4.shape)