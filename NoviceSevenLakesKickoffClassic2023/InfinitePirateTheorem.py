phrases = []
chars = "arghmteyARGHMTEY "
for i in range(int(input())):
    phrases.append(input())
for i in range(len(phrases)):
    fail = False
    for x in phrases[i]:
        if x not in chars:
            fail = True
    if fail:
        print("No")
    else:
        print("Yes")
