while True:
    try:
        name = input()
    except:
        break
    if name.endswith("s"):
        print(name + "aurus")
    else:
        print(name + "saurus")
# failed test case 1 because of extra spaces after the name, i realized this at like one minute left so i didn't have enough time to fix it sadly
