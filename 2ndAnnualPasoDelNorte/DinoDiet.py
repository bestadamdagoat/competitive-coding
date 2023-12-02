carnivore = []
herbivore = []
omnivore = []
sepdinodiet = []
while True:
    try:
        dinodiet = input()
    except:
        break
    sepdinodiet = dinodiet.split(", ")
    if sepdinodiet[1] == "Carnivore":
        carnivore.append(sepdinodiet[0])
    elif sepdinodiet[1] == "Herbivore":
        herbivore.append(sepdinodiet[0])
    elif sepdinodiet[1] == "Omnivore":
        omnivore.append(sepdinodiet[0])
print("Carnivore:")
print(*carnivore, sep=", ")
print("Herbivore:")
print(*herbivore, sep=", ")
print("Omnivore:")
print(*omnivore, sep=", ")
