while True:
    try:
        name, horizontald, verticald, speed = input().split(",")
    except:
        break
    horizontald = float(horizontald)
    verticald = float(verticald)
    speed = float(speed)
    distance = (horizontald**2 + verticald**2)**0.5
    if distance / speed <= 2:
        print('Dinner Time')
    else:
        print('Maybe Next Time')
