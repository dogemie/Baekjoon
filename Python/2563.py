array = [[0 for col in range(100)] for row in range(100)]
nn = int(input())
for i in range(nn):
    temp = [0,0]
    temp[0], temp[1] = map(int, input().split())
    for j in range(temp[1], temp[1] + 10):
        for k in range(temp[0], temp[0] + 10):
            array[j][k] = 1

result = 0
for i in range(100):
    for j in range(100):
        if array[i][j] == 1:
            result += 1
print(result)
            