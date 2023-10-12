score = 0
for x in range(int(input())):
    bar = str(input())
    if bar.count("1") > 1:
        score = score + 1
print(score)
