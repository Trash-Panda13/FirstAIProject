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
hunger = 100
energy = 100


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

#The thing idk
for row in grid:
    print(" ".join(row))