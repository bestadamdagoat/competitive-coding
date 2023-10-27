firstrun = True
added = 0
for i in input().split(" "):
    if firstrun:
        firstrun = False
        continue
    added = added + int(i)
print(added)
