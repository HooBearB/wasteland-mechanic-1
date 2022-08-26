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
        print("vehicles json not found")
        items = "None"
    return items

vehicles = loadFiles('vehicles')
parts = loadFiles('items')

list = vehicles["list"]
while 1 == 1:
    decision = askOption("Select listobj", list)
    chosenvehicle = list[decision - 1]
    print()
    print(vehicles[chosenvehicle]["name"])
    x = 0
    while x < len(vehicles[chosenvehicle]["display"]):
        print(vehicles[chosenvehicle]["display"][x])
        x = x + 1
    print()
    x = 0
    while x < len(vehicles[chosenvehicle]["sidedisplay"]):
        print(vehicles[chosenvehicle]["sidedisplay"][x])
        x = x + 1
    partlist = vehicles[chosenvehicle]
    decision = 0
    while decision != 3:
        decision = askOption("Vehicle menu", ["View parts", "View stats", "Get new car"])
        print()
        if decision == 1:
            print("Engine: " + parts[partlist["engine"]]["name"])
            print("Fuel tank: " + parts[partlist["fuel_tank"]]["name"])
            print("Radiator: " + parts[partlist["radiator"]]["name"])
            print("Battery: " + parts[partlist["battery"]]["name"])
            print("Transmission: " + parts[partlist["transmission"]]["name"])
            print("Suspension: " + parts[partlist["suspension"]]["name"])
            print("Tires: " + parts[partlist["tires"]]["name"])
            print("Headlights: " + parts[partlist["headlights"]]["name"])
            print("Taillights: " + parts[partlist["taillights"]]["name"])
            print("Radio: " + parts[partlist["radio"]]["name"])
        if decision == 2:
            print("Max speed: " + str(round((300 * (parts[partlist["engine"]]["hp"] ** (1/3))) / (partlist["weight"] ** (1/3)))) + "mph")
            print("Battery life: " + str(round(parts[partlist["battery"]]["charge"] / ((parts[partlist["headlights"]]["chargetaken"] * 2) + (parts[partlist["taillights"]]["chargetaken"] * 2) + parts[partlist["radio"]]["chargetaken"]), ndigits = 2)) + " hours")