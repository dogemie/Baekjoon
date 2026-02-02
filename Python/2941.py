cr = input() # String
num = 0
i = 0
while i < len(cr):
    if cr[i] != "c" and cr[i] != "d" and cr[i] != "l" and cr[i] != "n" and cr[i] != "s" and cr[i] != "z":
        num += 1
        # print("passed", cr[i], i)
    else:
        if cr[i] == "c":
            if i + 1 < len(cr):
                if cr[i + 1] == "=" or cr[i + 1] == "-":
                    num += 1
                    i += 1
                else:
                    num += 1
            else:
                num += 1
        elif cr[i] == "d":
            # print("check d", cr[i], i)
            if i + 1 < len(cr):
                if cr[i + 1] == "-":
                    # print("matched -", cr[i + 1], i + 1)
                    num += 1
                    i += 1
                elif cr[i + 1] == "z":
                    # print("check z", cr[i + 1], i + 1)
                    if i + 2 < len(cr):
                        if cr[i + 2] == "=":
                            # print("matched =", cr[i + 2], i + 2)
                            num += 1
                            i += 2
                        else:
                            num += 1
                    else:
                        num += 1
                else:
                    num += 1
            else:
                num += 1
        elif cr[i] == "l" or cr[i] == "n":
            # print("check ln", cr[i], i)
            if i + 1 < len(cr):
                if cr[i + 1] == "j":
                    # print("matched j", cr[i + 1], i + 1)
                    num += 1
                    i += 1
                    # print("after matched j", num, i)
                else:
                    num += 1
            else:
                num += 1
        elif cr[i] == "s" or cr[i] == "z":
            if i + 1 < len(cr):
                if cr[i + 1] == "=":
                    num += 1
                    i += 1
                else:
                    num += 1
            else:
                num += 1
    i += 1
    # print("end of while", num, i)
print(num)