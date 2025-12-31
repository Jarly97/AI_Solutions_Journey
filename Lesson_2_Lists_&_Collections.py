# #LESSON 2: Lists and Collections
# # Context: RPG Inventory System
# backpack = ["Torch", "Map"]

# backpack.append("Rope")
# backpack.append("Apple")

# print(f"Slot 0 contains: {backpack[0]}")
# print(f"Slot 2 contains: {backpack[2]}")
# print(backpack[-1])

#Context: Exercise - Listing Items in Inventory
backpack = []
backpack.append("Potion")
backpack.append("Axe")
backpack.append("Bread")
backpack.append("Key")
for item in backpack:
    if item == "Axe":
        print( "You have a: Axe (Equipped!)")
    else:
        print("You have a:", item)
    