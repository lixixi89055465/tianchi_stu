import numpy as np
arr=np.array([
    [1,1,-1],
    [0,-3,6]
])
print(arr)
print('1'*100)
print(np.ravel(arr, order='C'))
print(np.ravel(arr, order='F'))
print('2'*100)
print(np.ravel(arr, order='A'))

