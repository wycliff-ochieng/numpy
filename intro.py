import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[8.0, 9.0, 7.0],[3.0, 5.0, 4.0]])
print(b)
print(b.shape) #getting shape
print(b.ndim)#getting dimension

c = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(c)
print(c.shape)
print(c[1,5])
print(c[0,:])
print(c[:,6])

d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
print(d[0,1,1])

#initializing different types of arrays
# 1 and 0 only matrix
e = np.zeros((2,3,3,2))
print(e)

f = np.ones((4,2,4), dtype='int32')
print(f)

#any other number(full and full-like)
g = np.full((2,2),44)

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)

#copying arrays

#mathematics
k = np.array([2,3,4,5])
print(k+2)
print(k-2)
print(k**2)

print(np.sin(k))# cos, tan, 
#linear algebra
lin = np.ones((2,3))
print(lin)
alg = np.full((3,2),2)
print(alg)
print(np.matmul(lin,alg))

#statistics
