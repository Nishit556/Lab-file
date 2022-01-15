matrix1 = [[1,1,1], [1,1,1], [1,1,1]]
matrix2 = [[2,2,2], [2,2,2], [2,2,2]]

res = [[0 for x in range(3)] for y in range(3)]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]


print(res)
print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")

