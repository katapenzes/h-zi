
import math

def egy(x):
    min = math.inf
    max = -(math.inf)
    for i in x:
        if i<min:
            min = i
    for j in x:
        if j>max:
            max = j

    return min,max

x = [1,4,7,9,13,26,10,2]
print(egy(x))
