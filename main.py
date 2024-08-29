import math

def invalid_option():
    print("Invalid option, aborting...")
    quit()

print("Welcome to the online AR-600!\n") # Welcome message

sideNames = [ # Define valid letters for future input
    "o",
    "a",
    "h"
]

try: # To check if the input is an integer
    solvingFor = int(input("Are you solving for a missing side or a missing angle? (1 for side, 2 for angle): "))
except ValueError:
    invalid_option()
if int(solvingFor) == 1:
    # Gather data from user
    try:
        givenAngle = float(input("What is theta? (in degrees): "))
        unknownSide = input("What side are you trying to find? (o for opposite, a for adjacent, h for hypotenuse): ")
        if unknownSide not in sideNames:
            invalid_option()
        knownSide = input("Which side has a known length? (o for opposite, a for adjacent, h for hypotenuse): ")
        if knownSide not in sideNames:
            invalid_option()
        knownSideLength = float(input("What is the length of the known side? "))
    except ValueError:
        invalid_option()

    # Equations for solving all types of sides
    if unknownSide == "o" and knownSide == "h":
        solvedSideLength = knownSideLength*math.sin(math.radians(givenAngle))
    if unknownSide == "a" and knownSide == "h":
        solvedSideLength = knownSideLength*math.cos(math.radians(givenAngle))
    if unknownSide == "o" and knownSide == "a":
        solvedSideLength = knownSideLength*math.tan(math.radians(givenAngle))

    if unknownSide == "h" and knownSide == "o":
        solvedSideLength = knownSideLength/math.sin(math.radians(givenAngle))
    if unknownSide == "h" and knownSide == "a":
        solvedSideLength = knownSideLength/math.cos(math.radians(givenAngle))
    if unknownSide == "a" and knownSide == "o":
        solvedSideLength = knownSideLength/math.tan(math.radians(givenAngle))
    else:
        invalid_option()
    
    # Printing results

    units = input("What units are being used? ")
    print("The unknown side is " + str(round(solvedSideLength,2)) + " " + units + " in length.")

elif int(solvingFor) == 2:
    knownCombination = int(input("What combination of sides are known? (1 = The opposite and hypotenuse, 2 = The adjacent and hypotenuse, 3 = The opposite and adjacent): "))
    if knownCombination == 1:
        # Code for arcsin
        try:
            oppositeLength = float(input("What is the length of the opposite? "))
            hypotenuseLength = float(input("What is the length of the hypotenuse? "))
            solvedAngle = math.degrees(math.asin(oppositeLength/hypotenuseLength))
        except ValueError:
            invalid_option()
    if knownCombination == 2:
        # Code for arccos
        try:
            adjacentLength = float(input("What is the length of the adjacent? "))
            hypotenuseLength = float(input("What is the length of the hypotenuse? "))
            solvedAngle = math.degrees(math.acos(adjacentLength/hypotenuseLength))
        except ValueError:
            invalid_option()
    if knownCombination == 3:
        # Code for arctan
        try:
            oppositeLength = float(input("What is the length of the opposite? "))
            adjacentLength = float(input("What is the length of the adjacent? "))
            solvedAngle = math.degrees(math.atan(oppositeLength/adjacentLength))
        except ValueError:
            invalid_option()
    else:
        invalid_option()
    print("The solved angle is " + str(round(solvedAngle,2)) + " degrees")
else:
    invalid_option()
