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
energy = 100

healthScore = 100 - health
energyScore = 100 - energy

creaturey = 2
creaturex = 2

grid [creaturey][creaturex] = "C"

#The thing idk
for row in grid:
    print(" ".join(row))