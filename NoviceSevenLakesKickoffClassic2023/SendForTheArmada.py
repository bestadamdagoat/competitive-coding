alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
phrases = []
mod = []
newword = ""
global g
for i in range(int(input())):
    g = input()
    g.split(" ", 1)
    mod.append(g[0])
    phrases.append(g[1])
for i in range(len(phrases)):
    newword = ""
    for x in phrases[i]:
        placement = alphabet.find(x) + int(mod[i])
        if placement > 26:
            placement = placement - 26
        newword = newword + alphabet[placement]
    print(newword)

# fail - last minute program that i couldn't fix
# prints only one letter for some reason, although it prints correctly
