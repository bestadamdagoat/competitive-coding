dinos = []
bones = []
while True:
    try:
        dino = input()
    except:
        break
    dlist = dino.split(",")
    dinos.append(dlist[0])
    bones.append(int(dlist[1]))
print("Dinosaur with Most Bones: " + dinos[bones.index(max(bones))])
print("Dinosaur with Fewest Bones: " + dinos[bones.index(min(bones))])
print("Average Number of Bones: " + str(sum(bones)/len(bones)))
