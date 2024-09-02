def oddLines():
    f = open("Story.txt", "r")

    Counter = 0
    for i, line in enumerate(f):
        if i == Counter:
            print(line)
            Counter += 2
    f.close()

def evenLines():
    f = open("Story.txt", "r")

    Counter = 1
    for i, line in enumerate(f):
        if i == Counter:
            print(line)
            Counter += 2
    f.close()

def appendFirstLine():
    f = open("Story.txt", "w")
    f.write("test")
    f.close()
