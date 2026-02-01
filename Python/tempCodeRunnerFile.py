a = int(input())
b = a // 2 + a % 2
print(b)
for i in range(b):
    for j in range(b - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(b - 2, -1, -1):
    for j in range(b - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    if (i != 0):
        print()