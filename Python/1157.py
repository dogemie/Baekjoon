a = input()
a = a.lower()
bet = [0] * 26
for i in a:
    bet[ord(i) - ord('a')] += 1

cc = sorted(bet, reverse=True)
if cc[0] == cc[1]:
    print("?")

else:
    ch = -1 # 개수
    number = -1 # 알파벳 번호
    for i in range(26):
        if bet[i] > ch: # bet[i]도 개수니까 ch랑 비교
            ch = bet[i]
            number = i
    # print(bet)
    print(chr(number + ord('A')))
