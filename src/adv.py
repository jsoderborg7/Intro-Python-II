from room import Room
from player import Player
from item import Item

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

# Add items to rooms

room['outside'].items.append(
    [Item("Lamp", "Small oil lamp")])
room['overlook'].items.append(
    [Item("Telescope", "Small brass telescope")])
room['narrow'].items.append(
    [Item("Coins", "Several gold coins in odd sizes")])
room['treasure'].items.append(
    [Item("Scrap", "Scrap of paper, maybe a piece of a map?")])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Hermione", room['outside'])

# Inventory/item loops

def roomItems():
    if len(player.current_room.items) > 0:
      print('An item is hidden in this room:')
      for item in player.current_room.items:
        print(f"{item.get_item_name()}")

def playerInventory():
    if len(player.inventory) > 0:
        print(f"Here is your inventory: ")
        for item in player.inventory:
            print(f"{item.get_item_name()}")

def inventory():
    while True:
        playerInventory()
        interact = input("Choose from the following options: \n 'pickup' to add item to inventory \n 'drop' to remove item from inventory \n 'i' to check inventory \n 'move' to move on")
        if interact == 'move':
            break
        elif interact == 'i':
            print(playerInventory())
        elif len(interact.split(' ')) > 1:
            action = interact.split(' ')[0]
            itemName = interact.split(' ')[1]
            roomItems = [item.get_item_name() for item in player.current_room.get_room_items()]
            playerItems = [item.get_item_name() for item in player.inventory]

            if action == "pickup":
                if itemName in roomItems:
                    player.add_player_item(
                        player.current_room.get_room_items()[roomItems.index(itemName)])
                    player.current_room.remove_room_item(player.current_room.get_room_items()[
                                                    roomItems.index(itemName)])
                else:
                    print(f"Oops! {itemName} doesn't exist!")
            elif action == "drop":
                if itemName in playerItems:
                    player.current_room.add_room_item(
                        player.inventory[playerItems.index(itemName)])
                    player.remove_player_item(
                        player.inventory[playerItems.index(itemName)])
                else: 
                    print(f"Oops! {itemName} doesn't exist!")
            else:
                print("Please choose a valid option")



# Write a loop that:
#
# * Prints the current room name
def AdventureGame():
    print(f'\n{player.current_room}')

# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.current_room.description}")

    roomItems()

# * Waits for user input and decides what to do.
    while True:
        userInput = input(
            "\nEnter command n,s,e,w to move, q to quit\n")

        if userInput == ('n' or 's' or 'e' or 'w'):
            print(f"You have entered {userInput!r}")
        elif userInput == 'i':
            inventory()
        elif userInput == 'q':
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
                print(f"You have entered {player.current_room}")
                print(f"{player.current_room.description}")
                roomItems()

        if userInput == 's':
            print("Heading South!")
            if player.current_room.s_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.s_to
                print(f"You have entered {player.current_room}")
                print(f"{player.current_room.description}")
                roomItems()

        if userInput == 'e':
            print("Heading East!")
            if player.current_room.e_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.e_to
                print(f"You have entered {player.current_room}")
                print(f"{player.current_room.description}")
                roomItems()

        if userInput == 'w':
            print("Heading West!")
            if player.current_room.w_to == None:
                print("Oops, no room here! Please enter another command")
            else:
                player.current_room = player.current_room.w_to
                print(f"You have entered {player.current_room}")
                print(f"{player.current_room.description}")
                roomItems()

if __name__ == '__main__':
    AdventureGame()



#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
