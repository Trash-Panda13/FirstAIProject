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
food = 20

foody = 1
foodx = 4
grid[foody][foodx] = "F"

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
    if hungerScore > energyScore:
        print("Creature wants to eat")
        
        #Movement
        if creaturex < foodx:
            creaturex += 1
            hunger = max(hunger - 10, 0)
            energy = max(energy - 5, 0)
        elif creaturex > foodx:
            creaturex -= 1
            hunger = max(hunger - 10, 0)
            energy = max(energy - 5, 0)
        elif creaturey < foody:
            creaturey += 1
            hunger = max(hunger - 10, 0)
            energy = max(energy - 5, 0)
        elif creaturey > foody:
            creaturey -= 1
            hunger = max(hunger - 10, 0)
            energy = max(energy - 5, 0)
            
        #Food consumption
        if creaturex == foodx and creaturey == foody:
            hunger = min(hunger + food, 100)
            print("Creature has eaten the food")
            
            #Remove old food
            grid[foody][foodx] = "."

            #New food
            foody = random.randint(0, 4)
            foodx = random.randint(0, 4)
            
            #Make sure it doesn't spawn on the creature
            while foody == creaturey and foodx == creaturex:
                foody = random.randint(0, 4)
                foodx = random.randint(0, 4)
            
    elif energyScore > hungerScore:
        print("Creature wants to sleep")
        energy = min(energy + 10, 100)
        print("Creature has slept")
        
    else:
        hunger = max(hunger - 5, 0)
        print("Creature is content")
        
    #Grid update
    grid[oldy][oldx] = "."
    grid[creaturey][creaturex] = "C"
    
    #Grid Food
    grid[foody][foodx] = "F"

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