# Context: Multi-Character Inventory System

def show_inventory(character_name, gear_list, equipped_item):
    print(f"--- Inventory for {character_name} ---")
    for item in gear_list:
        if item == equipped_item:
            print(f"{item} (Equipped!)")
        else:
            print(item)
    print("----------------------------")

# Main Game Logic
hero_backpack = ["Potion", "Axe"]
goblin_backpack = ["Club", "Rock"]

# Function Calls
show_inventory("Hero", hero_backpack, equipped_item="Axe")
show_inventory("Goblin", goblin_backpack, equipped_item="Club")