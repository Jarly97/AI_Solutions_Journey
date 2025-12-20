#The World Map
rooms = {'Player House': {
    'description': 'You are standing in your home in the EAST of Gretish. The Tavern is to the WEST. The Fishing Hut is to the NORTH.',
    'paths': { 'north': 'Fishing Hut', 'west': 'Tavern'},
    'items': None
},
'Fishing Hut': {
    'description': ' The ocean breeze gently caresses your face. John is focused on his fishing rod cast into the water.',
    'paths': { 'south': 'Tavern', 'west': 'Forest'},
    'items': ['fish','fishing rod']
},
'Tavern':{
    'description': 'The Tavern seems fairly quiet this time of day. You see Fredrick behind the bar polishing tankards for the evening crowd.',
    'paths': { 'north': 'Fishing Hut', 'west': 'Forest', 'east': 'Player House'},
    'items': ['barrel', 'tankard']
},
'Forest': {
    'description': 'The forest of Gretish is home to many creatures and flora. You should approach with caution.',
    'paths': {'east': 'Tavern', 'north': 'Fishing Hut'},
    'items': ['mushroom']
},
}

#Player State
player={
    'location': 'Player House',
    'inventory':[]
}
#The Game Engine
while True:
    # 1. Get current location
    current_room_name = player['location']
    current_room_data = rooms[current_room_name]

    # 2. Print Description
    print(f"\n---You are in the {current_room_name}.---")
    print(current_room_data['description'])
    
    # 3. Get Player Input
    command = input(">").lower().strip()

    # 4. Handle Exit
    if command == 'exit' or command == 'quit':
        print("Thanks for playing!")
        break

    # 5. Handle Movement
    elif command in ['north', 'south', 'east', 'west']:
        if command in current_room_data['paths']:
            new_location = current_room_data['paths'][command]
            player['location'] = new_location
            print(f"You move {command} to the {new_location}.")
        else:
            print("You can't go that way.")

    # 6. Handle Unknown Commands
    else:
        print("I dont understand that command.")