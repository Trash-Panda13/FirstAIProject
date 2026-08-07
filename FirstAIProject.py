import random

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

creaturey = 2
creaturex = 2
grid [creaturey][creaturex] = "C"

#Food
berry = 25

berryy = 1
berryx = 4
grid[berryy][berryx] = "F"

#AI
while health > 0 and hunger > 0 and energy > 0:
    
    #Decision making
    healthScore = 100 - health
    hungerScore = 100 - hunger
    energyScore = 100 - energy
    
    #Old position
    oldx = creaturex
    oldy = creaturey

    #Decision making
    if hungerScore >= energyScore:
        print("Creature wants to eat")
        
        #Movement
        if creaturex < berryx:
            creaturex += 1
            hunger = max(hunger - 5, 0)
            energy = max(energy - 3, 0)
        elif creaturex > berryx:
            creaturex -= 1
            hunger = max(hunger - 5, 0)
            energy = max(energy - 3, 0)
        elif creaturey < berryy:
            creaturey += 1
            hunger = max(hunger - 5, 0)
            energy = max(energy - 3, 0)
        elif creaturey > berryy:
            creaturey -= 1
            hunger = max(hunger - 5, 0)
            energy = max(energy - 3, 0)
            
        #Food consumption
        if creaturex == berryx and creaturey == berryy:
            hunger = min(hunger + berry, 100)
            print("Creature has eaten the berry")
            
            #Remove old berry
            grid[berryy][berryx] = "."

            #New berry
            berryy = random.randint(0, 4)
            berryx = random.randint(0, 4)
            
            #Make sure it doesn't spawn on the creature
            while berryy == creaturey and berryx == creaturex:
                berryy = random.randint(0, 4)
                berryx = random.randint(0, 4)
            
    elif energyScore > hungerScore:
        print("Creature wants to sleep")
        hunger = max(hunger - 5, 0)
        energy = min(energy + 10, 100)
        print("Creature has slept")
        
    else:
        hunger = max(hunger - 5, 0)
        print("Creature is content")
        
    #Grid update
    grid[oldy][oldx] = "."
    grid[creaturey][creaturex] = "C"
    
    #Grid Food
    grid[berryy][berryx] = "F"

    #The thing idk
    print("Health:", health)
    print("Hunger:", hunger)
    print("Energy:", energy)
    print()
    
    for row in grid:
        print(" ".join(row))
        
    print()
    input("Press Enter to continue...")
        
print("Creature has died")