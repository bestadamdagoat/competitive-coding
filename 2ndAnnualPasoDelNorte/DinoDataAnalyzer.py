name = []
diet = []
length = []
weight = []
while True:
    try:
        dino = input()
    except:
        break
    dlist = dino.split(",")
    name.append(dlist[0])
    diet.append(dlist[1])
    length.append(float(dlist[2]))
    weight.append(float(dlist[3]))
print("Average Length: " + str(sum(length)/len(length)))
print("Average Weight: " + str(sum(weight)/len(weight)))
print("Largest Dinosaur (by weight): " + name[weight.index(max(weight))])
print("Longest Dinosaur (by length): " + name[length.index(max(length))])
print("Number of Carnivores: " + str(diet.count("Carnivore")))
print("Number of Herbivores: " + str(diet.count("Herbivore")))
print("Number of Omnivores: " + str(diet.count("Omnivore")))
