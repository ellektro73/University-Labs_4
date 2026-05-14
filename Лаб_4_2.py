size = 7

matrix = [[0 for j in range(size)] for i in range(size)]

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            matrix[i][j] = 1

print(f"Масив {size}x{size}:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()