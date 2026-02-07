array = [0] * 5

for i in range(5):
    array[i] = input()
for i in range(15):
    for j in range(5):
        if i < len(array[j]):
            print(array[j][i], end="")