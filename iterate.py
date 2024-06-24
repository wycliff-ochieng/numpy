import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
for x in np1:
    print(x)

#2-d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for y in np2:
    print(y) 
    for z in y:
        print(z)

np3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
for a in np3:
    print(a)
    for b in a:
        print(b)
        for c in b:
            print(c)

#use np.nditer to loop directly
np4  = np.array([[[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]])
for d in np.nditer(np4):
    print(d)
