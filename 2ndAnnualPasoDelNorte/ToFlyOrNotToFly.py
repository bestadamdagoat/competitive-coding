dinos = []
for i in range(int(input())):
    dinos.append(input())
for i in dinos:
    if "pt" in i:
        print("YES")
    else:
        print("NMI")
