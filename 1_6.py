'''
Given an image represented by
an NxN matrix, where each pixel
in the image is 4 bytes,
write a method to rotate the image
by 90 degrees.
Can you do this in place?
'''
N = 5
def transpose(matrix):
    N = len(matrix)
    new_matrix = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(matrix[j][i])
        new_matrix.append(temp)
    return new_matrix
        
#create matrix
matrix = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(i * 5 + j)
    matrix.append(temp)

print(transpose(matrix))