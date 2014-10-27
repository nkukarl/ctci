'''
Write an algorithm such that
if an element in an MxN matrix is 0,
its entire row and column is set to 0.
'''

import random

def set_zeros(matrix):
    rows = []
    columns = []
    M = len(matrix)
    N = len(matrix[0])
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                if i not in rows:
                    rows.append(i)
                if j not in columns:
                    columns.append(j)
    
    for i in range(M):
        for j in columns:
            matrix[i][j] = 0
            
    for i in rows:
        for j in range(N):
            matrix[i][j] = 0
    
    return matrix


# create a MxN matrix
M = 5
N = 5
K = 2 # number of zeros

lst = list(range(1, M * N - K + 1))
for i in range(K):
    lst.append(0)
random.shuffle(lst)

idx = 0
matrix = []
for i in range(M):
    temp = []
    for j in range(N):
        temp.append(lst[idx])
        idx += 1
    matrix.append(temp)

print(matrix)
print(set_zeros(matrix))