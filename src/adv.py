from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items=['lantern']), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items=['telescope']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items=['pile of coins']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Hermione", room['outside'])

while True:
    itemsInRoom = player.current_room.items

    print(f"{player.name} is located {player.current_room.name}")


    for item in itemsInRoom:
        print(f"You found a {item}")

    # Commands
    cmd = input("\nPlease choose 'n,s,w,e' to move, 'get' to take item, 'drop' to drop item, or 'q' to quit\n")

    # Action commands

    if len(cmd) > 1:
        action = cmd.split(' ')
        if action[0] == 'get':
            if action[1] in itemsInRoom:
                player.current_room.removeItem(action[1])
                player.pickupItem(action[1])
            else:
                print("Sorry, that item doesn't exist here!")
        elif action[0] == 'drop':
            if action[1] in player.items:
                player.current_room.addItem(action[1])
                player.dropItem(action[1])

    # Inventory commands

    if cmd == 'i':
        if len(player.items) > 0:
            print('Your Inventory: ')
            for item in player.items:
                print(f"{item}")

    # Direction commands

    if cmd == 'n':
        if player.current_room.n_to is None:
            print("Oops! No room that way, please choose another direction!")
        else:
            player.current_room = player.current_room.n_to
    elif cmd == 's':
        if player.current_room.s_to is None:
            print("Oops! No room that way, please choose another direction!")
        else:
            player.current_room = player.current_room.s_to
    elif cmd == 'w':
        if player.current_room.w_to is None:
            print("Oops! No room that way, please choose another direction!")
        else:
            player.current_room = player.current_room.w_to
    elif cmd == 'e':
        if player.current_room.e_to is None:
            print("Oops! No room that way, please choose another direction!")
        else:
            player.current_room = player.current_room.e_to
    elif cmd == 'q':
        print("Thanks for playing!")
        break

# Write a loop that:
#
# * Prints the current room name
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
