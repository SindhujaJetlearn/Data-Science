#Addition of 2 matrix
print("\nAddtion of 2 matrix")

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [8, 9]]
result = [[0, 0], [0, 0]]

for i in range(0, 2):
  for j in range(0, 2):
    result[i][j] = matrixA[i][j] + matrixB[i][j]

#Print the result
for i in range(0, 2):
  for j in range(0, 2):
    print(result[i][j], end=" ")
  print("\n")
