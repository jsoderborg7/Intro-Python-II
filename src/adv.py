from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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

# Write a loop that:
#
# * Prints the current room name
def AdventureGame():
    print({player.current_room})

# * Prints the current description (the textwrap module might be useful here).
    print({player.current_room.descripton})

# * Waits for user input and decides what to do.
    while True:
        userInput = input(
            "Enter command n,s,e,w to move, q to quit")

        if userInput == ('n' or 's' or 'e' or 'w'):
            print("you have entered {userInput!r}")
        elif userInput == ('q'):
            print("Thanks for playing!")
            break
        else:
            print("Please enter valid command")

        if userInput == 'n':
            print("Heading North!")
            if player.current_room.n_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.n_to
                print("You have entered {player.current_room}")
                print({player.current_room.description})

        if userInput == 's':
            print("Heading South!")
            if player.current_room.s_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.s_to
                print("You have entered {player.current_room}")
                print({player.current_room.description})

        if userInput == 'e':
            print("Heading East!")
            if player.current_room.e_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.e_to
                print("You have entered {player.current_room}")
                print({player.current_room.description})

        if userInput == 'w':
            print("Heading West!")
            if player.current_room.w_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.w_to
                print("You have entered {player.current_room}")
                print({player.current_room.description})

if __name__ == '__main__':
    AdventureGame()



#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
