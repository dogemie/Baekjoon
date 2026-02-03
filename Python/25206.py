total = 0
grade = 0
for i in range(20):
    data = list(map(str, input().split(" ")))
    if data[2] == "P":
        continue
    elif data[2] == "A+":
        total += 4.5 * float(data[1])
    elif data[2] == "A0":
        total += 4.0 * float(data[1])
    elif data[2] == "B+":
        total += 3.5 * float(data[1])
    elif data[2] == "B0":
        total += 3.0 * float(data[1])
    elif data[2] == "C+":
        total += 2.5 * float(data[1])
    elif data[2] == "C0":
        total += 2.0 * float(data[1])
    elif data[2] == "D+":
        total += 1.5 * float(data[1])
    elif data[2] == "D0":
        total += 1.0 * float(data[1])
    elif data[2] == "F":
        total += 0.0 * float(data[1])
    grade += float(data[1])
total_output = total / grade
print(total_output)