l = []
for i in range(int(input())):
    d = input().split("Simon says")
    if len(d) > 1:
        l.append(d[1])
for i in l:
    print(i)