num = int(input())

check = 0

for i in range(num):
    gr = input()
    par = [0] * 26
    j = 0
    tt = 0
    while j < len(gr):
        if par[ord(gr[j]) - ord('a')] > 0:
            tt += 1
            break
        par[ord(gr[j]) - ord('a')] += 1
        while True:
            if j + 1 >= len(gr):
                break
            if gr[j] == gr[j + 1]:
                j += 1
            else:
                break
            
        j += 1
    if tt == 0:
        check += 1
print(check)