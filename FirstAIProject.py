#The world
grid = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

#Creature
health = 100
hunger = 80
energy = 60

healthScore = 100 - health
hungerScore = 100 - hunger
energyScore = 100 - energy

creaturey = 2
creaturex = 2
grid [creaturey][creaturex] = "C"

#Food
food = 20

foody = 1
foodx = 4
grid[foody][foodx] = "F"

#AI
#Movement
distance = abs(creaturex - foodx) + abs(creaturey - foody)

#Decision making
if hungerScore > energyScore:
    print("Creature wants to eat")
    if creaturex < foodx:
        creaturex += 1
        hunger -= 10
        energy -= 5
    elif creaturex > foodx:
        creaturex -= 1
        hunger -= 10
        energy -= 5
    elif creaturey < foody:
        creaturey += 1
        hunger -= 10
        energy -= 5
    elif creaturey > foody:
        creaturey -= 1
        hunger -= 10
        energy -= 5
elif energyScore > hungerScore:
    print("Creature wants to sleep")
    energy += 10
else:
    print("Creature is content")

#The thing idk
for row in grid:
    print(" ".join(row))