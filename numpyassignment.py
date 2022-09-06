import numpy as np

'''
0-D: [2]
1-D: [3, 4, 5, 6, 7]
2-D: [[8, 1, 3], [2, 3, 4], [6, 2, 5]]
3-D: [[[1, 2, 4], [3, 3, 2], [1, 9, 1]], [[6, 8, 7], [9, 1, 0], [8, 2, 3]], [[5, 4, 1], [5, 7, 2], [3, 5, 9]]]
'''
D0 = np.array(2)
print('D0 ==============================')
print(D0)

D1 = np.array([3, 4, 5, 6, 7])
print('D1 ==============================')
print(D1)

D2 = np.array([[8, 1, 3], [2, 3, 4], [6, 2, 5]])
print('D2 ==============================')
print(D2)

D3 = np.array([[[1, 2, 4], [3, 3, 2], [1, 9, 1]], [[6, 8, 7], [9, 1, 0], [8, 2, 3]], [[5, 4, 1], [5, 7, 2], [3, 5, 9]]])
print('D3 ==============================')
print(D3)

'''
Use index to change all value 8 to 100 in 4 arrays
'''
D2[0, 0] = 100
print(D2)

D3[1, 0, 1] = 100
D3[1, 2, 0] = 100
print(D3)

'''
    a. the value of 0-D array
	b. the middle of 1-D array
	c. the center of 2-D array
	d. the center of 3-D array ( the center of middle 2-D array )
'''
sum = D0 + D1[2] + D2[1, 1] + D3[1, 1, 1]
print('total sum is: ' + str(sum))

class myClass:
    def __init__(self):
        pass

myObj = myClass()