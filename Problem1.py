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
    f = open("Story.txt", "r")
    OG = f.read()
    f = open("Story.txt", "w")
    f.write("Once upon a time" + "\n" + "\n" + OG)
    f.close()

def appendLastLine():
    f = open("Story.txt", "r")
    OG = f.read()
    f = open("Story.txt", "w")
    f.write(OG + "\n" + "the End")
    f.close()

def create4newLines():
    f = open("Story.txt", "r")
    nf = open("4lines.txt", "w")
    for i in range(4):
        line = f.readline()
        nf.write(line)
    f.close()
    nf.close()
def deletefirstLine():
    nf = open("4lines.txt", "r")
    line = nf.readlines()
    nf = open("4lines.txt", "w")
    nf.writelines(line[1:])
    nf.close()
deletefirstLine()

