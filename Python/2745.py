data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string, num = input().split()
num = int(num)
result = 0
for i in range(len(string)):
    result += data.index(string[len(string) - 1 - i]) * (num ** i)
    
print(result)