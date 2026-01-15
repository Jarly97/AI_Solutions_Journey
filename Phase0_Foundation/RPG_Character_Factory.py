#Objective 1: Creating a Factory Pattern for text RPG
#This module defines a factory for creating RPG character instances.
#Goal:Writing a function that generates character objects based on specified attributes.
#Task: Return a dictionary representing the character with keys: name, role, hp, and inventory.

#Example Usage:
# character1 = create_char("Aragorn", "Warrior")    
# print(character1)# Expected Output:
# {"name": "Aragorn", "role": "Warrior", "hp": 120, "inventory": [] }
# character2 = create_char("Gandalf", "Mage")
# print(character2) # Expected Output:
# {"name": "Gandalf", "role": "Mage", "hp": 100, "inventory": [] }

name= input("Enter character name: ").lower()
role= input("Enter character role (e.g., Warrior, Mage, Archer, Priest): ").lower()

def create_char(name,role):
    if role == "warrior":
        hp = 120
    else:
        hp = 100

    create_char = {
        "name": name,
        "role": role,
        "hp": hp,
        "inventory": []
    }
    return create_char
character = create_char(name, role)
print(character)

#Objective 2: Combat Engine Simulation
#This module simulates a simple combat engine for RPG characters.
#Goal: Writing a function that simulates an attack from one character to another.
#Task: Reduce the target character's hp by a fixed damage amount and return the updated target character.

def combat_encounter(character, monster_hp, damage=15):
    while monster_hp >0:
        monster_hp -= damage
        
        if monster_hp < 0:
            monster_hp = 0
        print ("Player Attacks! Monster HP is now:", monster_hp)

        if monster_hp == 0:
            break

    print("Monster Defeated!")
    return character

#Objective 3: Integration of Character Factory and Combat Engine
#This module integrates the character factory and combat engine to simulate a battle scenario.
#Task: Write main_game_logic that connects Factrory and Combat Engine.
#Goal: Create a character and simulate a combat encounter with a monster, with loot drop upon victory.

def main_game_logic():
    character = create_char(name, role)
    print("Character Created:", character)

    monster_hp = 40
    print("A wild monster appears with HP:", monster_hp)

    updated_character = combat_encounter(character, monster_hp)

    loot = "Golden Key"
    updated_character["inventory"].append(loot)
    print("Loot Acquired:", loot)
    print("Updated Character:", updated_character)
    
    
main_game_logic()