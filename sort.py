import numpy as np

np1 = np.array([6,7,4,0,2,1,3])
print(np1)
print(np.sort(np1))

#alphabetical
np2 = np.array(['joy','alexis','faith','wycliff','charity'])
print(np2)
print(np.sort(np2))

#boolean

np3 = np.array([True,False,True,True,False,False,False,False])
print(np3)
print(np.sort(np3))

print(np1) #original
print(np.sort(np1)) # copy-does not affect original
print(np1)

#2-d
np4 = np.array([[4,8,6,1,17,5],[9,2,7,3,0,10]])
print(np4)
print(np.sort(np4))