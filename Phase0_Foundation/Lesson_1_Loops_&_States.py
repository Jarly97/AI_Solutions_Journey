
#LESSON 1: Loops and State
# Context: Character movement mechanism

energy = 15

while energy > 5:
    print("Character moves forward")
    energy = energy - 5

print("Character is out of energy and needs to rest.")

#Context: Resting mechanism

while energy < 10:
    print("Character is resting" + ". Current energy:", energy)
    energy = energy + 1
print("Character has regained enough energy to move again.")

# The invisible state
print(f"REAL FINAL VALUE: {energy}")