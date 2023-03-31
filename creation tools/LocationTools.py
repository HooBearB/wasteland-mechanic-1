import os
import json

def askOption(message, options, indent = 2, lookingFor = -1):
    print()
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    runline = 0
    while runline < len(options):
        if runline == lookingFor:
            print("  - " + format.bold, end = "")
        else:
            run = 0
            while run <= indent + 1:
                print(" ", end = "")
                run = run + 1
        print(str(runline + 1) + ". " + options[runline])
        runline = runline + 1
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    while type(decision) != int:
        try:
            decision = int(decision)
        except:
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            print("Invalid input!")
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            decision = input("> ")
    while decision < 1 or decision > len(options):
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        print("Invalid input!")
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        decision = input("> ")
        while type(decision) != int:
            try:
                decision = int(decision)
            except:
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                print("Invalid input!")
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                decision = input("> ")
    return decision

def loadFiles(name):
    print()
    directory = os.path.dirname(__file__)
    print(directory)
    newdirectory = os.path.dirname(directory)
    print(newdirectory)
    filename = newdirectory + r'/json/' + name + r'.json'
    print(filename)
    try:
        items = json.load(open(filename, "r"))
    except:
        print("locations json not found")
        items = "None"
    return items

locations = loadFiles('locations')

list = locations["list"]
while 1 == 1:
    decision = askOption("Select listobj", list)
    chosenlocation = list[decision - 1]
    print()
    print(locations[chosenlocation]["name"])
    x = 0
    while x < len(locations[chosenlocation]["display"]):
        print(locations[chosenlocation]["display"][x])
        x = x + 1
    print()
    x = 0
    decision = 0