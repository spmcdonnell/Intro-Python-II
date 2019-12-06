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
earlier adventurers. The only exit is to the south.""")
}

# Declare all the items

item = {
    'gold': Item('Gold', 'An unfathomably large pile of gold'),

    'key': Item('Key', 'A key that grants access to the treasure room'),

    'mud': Item('Mud', 'Some mud. Useless.')
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

# Room Map (for developer reference)

########################################
#    Overlook    #######    Treasure   #
#                #######               #
#                #######     (gold)    #
#                #######               #
#                #######               #
########   ###################---#######
#     Foyer      #######     Narrow    #
#                #######               #
#                                      #
#                #######               #
#                #######               #
########   #############################
#    Outside     #######################
#                #######################
#                #######################
#                #######################
#                #######################
########################################

# Add items to rooms

room['treasure'].items.append(item['gold'])
room['overlook'].items.append(item['key'])
room['overlook'].items.append(item['mud'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def initialize():
    ###########################################
    # Set up player and orient them in the game
    ###########################################
    player_name = input('What is your name?\n')

    current_player = Player(player_name, room['outside'])

    nl = '\n'

    print(
        f'Welcome {current_player.get_name()}! Your current location is: {current_player.get_location().name}\n'
    )

    ################
    # Start movement
    ################
    def print_current_location():
        print(f'You are now in the {current_player.get_location().name}\n')

    def is_valid_move(move):
        if move != None:
            return True
        else:
            return False

    def room_has_items(room):
        if len(room.items):
            return True
        else:
            return False

    def print_items_message(room):
        print(
            f'This room is not empty! It contains:{nl}{nl.join(str(x.name) for x in room.items)}{nl}')

    while True:
        player_input = input('Take action:\n')

        if len(player_input.split()) == 1:
            if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
                if player_input == 'n':
                    if is_valid_move(current_player.get_location().n_to):
                        current_player.set_location(
                            current_player.get_location().n_to
                        )

                        print_current_location()

                        if room_has_items(current_player.get_location()):
                            print_items_message(current_player.get_location())
                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )

                elif player_input == 's':
                    if is_valid_move(current_player.get_location().s_to):
                        current_player.set_location(
                            current_player.get_location().s_to
                        )

                        print_current_location()

                        if room_has_items(current_player.get_location()):
                            print_items_message(current_player.get_location())
                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )

                elif player_input == 'e':
                    if is_valid_move(current_player.get_location().e_to):
                        current_player.set_location(
                            current_player.get_location().e_to
                        )

                        print_current_location()

                        if room_has_items(current_player.get_location()):
                            print_items_message(current_player.get_location())
                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
                else:
                    if is_valid_move(current_player.get_location().w_to):
                        current_player.set_location(
                            current_player.get_location().w_to
                        )

                        print_current_location()

                        if room_has_items(current_player.get_location()):
                            print_items_message(current_player.get_location())
                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
            elif player_input == 'i' or player_input == 'inventory':
                if len(current_player.items):
                    print(
                        f'You currently have:{nl}{nl.join(str(x.name) for x in current_player.items)}{nl}'
                    )
                else:
                    print('You don\'t have anything!')
            elif player_input == 'q':
                print(
                    f'Goodbye {current_player.get_name()}, we hope you\'ll play again!')
                break
            else:
                print(
                    'Invalid command: Navigate using "n", "s", "e", or "w", or check your inventory with "i", or press "q" to quit'
                )
        else:
            split_input = player_input.split()

            if split_input[0] == 'take' or split_input[0] == 'drop':
                if split_input[0] == 'take':
                    if room_has_items(current_player.get_location()):
                        current_player.items.append(
                            item[split_input[1].lower()])
                        current_player.location.items.remove(
                            item[split_input[1].lower()]
                        )

                        print(
                            f'You got: {current_player.items[len(current_player.items) - 1].name}!{nl}'
                        )
                else:
                    current_player.items.remove(item[split_input[1]])
                    current_player.location.items.append(
                        item[split_input[1]]
                    )

                    print(
                        f'You dropped: {current_player.location.items[len(current_player.items) - 1].name}!{nl}'
                    )
            else:
                print(
                    'Invalid command: use either "take" or "drop" to interact with items'
                )


initialize()
