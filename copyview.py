import numpy as np

np3 = np.array([1,2,3,4,5,6,7,8,9])
 
np2 = np3.view() # .view changes in original affect the copy

print(f'original NP3 {np3}')
print(f'original NP2 {np2}')

np3[0] = 41
np3[2] = 79

print(f'changed NP3 {np3}')
print(f'changed NP2 {np2}')

np4 = np3.copy() #.copy chnages in original does not affect the copy

print(f'original NP3 {np3}')
print(f'original NP4 {np4}')

np3[1] = 85
np3[5] = 97

print(f'changed NP3 {np3}')
print(f'changed NP4 {np4}')