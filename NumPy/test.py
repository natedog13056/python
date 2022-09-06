import numpy as np

zeroDarr = np.array([2])
print(zeroDarr)

oneDarr = np.array([3, 4, 5, 6, 7])
print(oneDarr)

twoDarr = np.array([[8, 1, 3], [2, 3, 4], [6, 2, 5]])
twoDarr[0, 0] = 100
print(twoDarr)

# print(twoDarr[2, 0])

threeDarr = np.array([[[1, 2, 4], [3, 3, 2], [1, 9, 1]], [[6, 8, 7], [9, 1, 0], [8, 2, 3]], [[5, 4, 1], [5, 7, 2], [3, 5, 9]]])
threeDarr[1, 0, 1] = 100
print(threeDarr)

#print(threeDarr[2, 1, -1])