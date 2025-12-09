# List

numbers = [2, 4, 5, 6, 9]

total = sum(numbers)

print("List:", numbers)

# Tuple

fruits = ("apple", "banana", "grapes", "mango")

print("first fruit:" ,fruits[0])
print("second fruit:", fruits[1])
print("total fruits:", len(fruits))

# Numpy

import numpy as np

array = np.array([5, 10, 15, 20])

print("Array:" , array)
print("Mean:", np.mean(array))
print("Max:", np.max(array))
print("Min:", np.max(array))
print("Min:" ,np.min(array))

# Pandas

import pandas as pd

data = {
    "Name" : ["Kusuma" , "Smitha" , "Kavya"],
    "Age" : [20, 21, 23],
    "City" : ["AP" , "Karnataka" , "Tamil Nada"]
}

df = pd.DataFrame(data)


print(df)
print("\nAverage Age:", df["Age"].mean())






