import numpy as np
import random

#123 represents first row #456 represent second row. rows and columns
arr01 = np.array([[1,2,3],[4,5,6]])

arr02 = np.array([0.0,0.1,0.2,0.3,0.4,0.5])

for row in arr01:
    print(row)
    for col in row:
        print(col,end=' ')
    print()


    for i in arr01.flat:
        print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2,4),dtype=int)

arr05 = np.full((3,5),13)


exercise = np.array([[random.randint(1,10)for i in range(5)],[random.randint(1,10)for i in range(5)]])

print(exercise)

b = np.array(np.random.randint(1,10,size= (2,5)))

print(b)





arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange(10,1,-2)


print()