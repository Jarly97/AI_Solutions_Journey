#The World Map
rooms = {'Player House': {
    'description': 'You are standing in your home in the EAST of Gretish. The Tavern is to the WEST. The Fishing Hut is to the NORTH.',
    'paths': { 'north': 'Fishing Hut', 'west': 'Tavern'},
    'items': None
},
'Fishing Hut': {
    'description': ' The ocean breeze gently caresses your face. John is focused on his fishing rod cast into the water.',
    'paths': { 'south': 'Tavern', 'west': 'Forest'}
    'items': ['fish', 'fishing rod']
}
'Tavern':{
    'description': 'The Tavern seems fairly quiet this time of day. You see Fredrick behind the bar polishing tankards for the evening crowd.',
    'paths': { 'north': 'Fishing Hut', 'west': 'Forest', 'east' 'Player House', }
    'items': ['barrel', 'tankard']
}
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