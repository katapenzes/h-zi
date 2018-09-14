
import numpy as np

def harom(m,n):
    x = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            x[i][j] = i*j
    return x

m = 3
n = 4
print(harom(m,n))
