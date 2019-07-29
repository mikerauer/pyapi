#!/usr/bin/python3


# Replace RPG starter project with this coe when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]

    To win get to the Garden
    with the skel_key and potion
    
    **Avoid Monster**
    ''')

def showStatus():
    #print the players current status
    print('-------------------------')
    print('You are in the ' + currentRoom)
    #print the current inv.
    print('Inventory : ' + str(inventory))
    #print am item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('-------------------------')

# an inv, which is initially emtpy
inventory = []

#a dict linking a room to ther rooms
rooms = {
            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining',
                'item' : 'skel_key'
                },

            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
                },
            
            'Dining' : {
                'west' : 'Hall',
                'item' : 'potion',
                'south' : 'Garden'
                },

            'Garden' : {
                'north' : 'Dining'
                }
            }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()
    
    #get the player's next 'move'
    move = ''
    while move =='':
        move = input('> ')
    
    # lowers cap, and splits on whitespace into a list ['go', 'east']
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed whatever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
             print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inv
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isnt there to get
        else:
            #tell them they cant get it
            print('Can\'t get ' + move[1] + '!')
    # if a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A Monster has got you....GAME OVER!')
        break

    # define how a player can win
    if currentRoom == 'Garden' and 'skel_key' in inventory and 'potion' in inventory:
        print('You escaped the house wit the ultra rare key and magic potion... You WIN!!!')
        break
