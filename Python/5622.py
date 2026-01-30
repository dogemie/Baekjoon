a = input()
b = len(a)
d = 0
for i in range(b):
    c = ord(a[i])
    if c >= 65 and c <= 67:
        d += 2
    elif c >= 68 and c <= 70:
        d += 3
    elif c >= 71 and c <= 73: #GHI
        d += 4
    elif c >= 74 and c <= 76: #JKL
        d += 5
    elif c >= 77 and c <= 79: #MNO
        d += 6
    elif c >= 80 and c <= 83: #PQRS
        d += 7
    elif c >= 84 and c <= 86: #TUV
        d += 8
    elif c >= 87 and c <= 90: #WXYZ
        d += 9
print(d+b)
