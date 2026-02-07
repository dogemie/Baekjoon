array = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    array[i] = list(map(int, input().split()))
max_value = -1
max_index = (0, 0)
for i in range(9):
    for j in range(9):
        if array[i][j] > max_value:
            max_value = array[i][j]
            max_index = (i + 1, j + 1)
print(max_value)
print(max_index[0], max_index[1])