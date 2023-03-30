import numpy as np
'''
integers = np.array([1,2,3])

print(type(integers))
print(integers)

#LIST COMPREHENSION
#create a one-dimensional array from a list comprehension that
#produces even integers from 2 through 20

even_integers = np.array([i for i in range(2,21,2)])
print(even_integers)

integers = np.array([[1,2,3],[4,5,6]])

print(integers)

print(integers.dtype)

print(integers.ndim)

print(integers.min())

print(integers.shape)

for row in integers:
    print(row)
    #print()
    for col in row:
        print(col, end=" ")
    print()

for i in integers.flat:
    print(i, end=" ")

print(np.zeros(5))

print(np.ones((2,4), dtype=int))

print(np.full((3,5), 13))

print(np.arange(5))

print(np.arange(5,10))

print(np.arange(10,1,-2))

print(np.linspace(0.0, 1.0, num=5))

array1 = np.arange(1,21)
print(array1)
array2 = array1.reshape(4,5)
print(array2)

array3 = np.arange(1,100001).reshape(4,25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)

numbers = np.arange(1,6)
print(numbers * 2)
twos = np.full(5,2)
print(twos)
print(numbers * twos)

print(numbers ** 3)

numbers += 10
print(numbers)

'''

grades = np.array([[87, 96, 70],[100,87,90],[94,77,90],[100,81,82]])

print(grades)
print(grades.sum())
print(grades.min())
print(grades.mean())
print(grades.std())

print(grades.mean(axis=0))   #by column or also by exam score
print(grades.mean(axis=1))   #by row or also by student score












