#!/usr/bin/env python3

# import sys
import numpy as np

# lista los parametros de entrada
# print(sys.argv)

arr = np.array([[-8, -7, 1, 5, 9], [-9, -5, -1, 7, 8], [-9, -7, 2, 4, 10],
                [-10, -4, -2, 7, 9], [-18, -17, 1, 14, 20]])

print(arr)

uniques, index_unq = np.unique(np.sort(np.abs(arr)), return_index=True, axis=0)
print(arr[index_unq])

print("Solo queria practicar")
