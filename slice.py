import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#from 1-4
print(np1[1:5])

#from 3 to end
print(np1[3:])

#from -5 to -3
print(np1[-5:-3])

#for beginning to 7 in steps of 2
print(np1[:7:2])

print(np1[::2])

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1,2])

#slicing 2-d
print(np2[0:1,1:3]) #alt print(np2[0:2,1:3])