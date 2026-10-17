
  # Kyle Gaston
# IT-140 Introduction to Scripting
# Project Two: Sand Rail Text-Based Adventure Game

def show_instructions():
    """Print the game title, objective, and available movement/item commands."""
    print("----------------------------------------------------------------------")
    print("             Sand Rail Bounty Hill Competition Game                   ")
    print("----------------------------------------------------------------------")
    print("Objective: Gather all 6 performance and safety upgrades before rolling ")
    print("up to the Starting Line, or fail tech inspection/lose the climb!")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get '<item name>'")
    print("Type 'exit' to quit the game.")
    print("----------------------------------------------------------------------")

def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and any item in the room."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    
    # Check if there is an item in the current room and display it if present
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        # Only show the item if it hasn't already been picked up
        if item not in inventory:
            print(f"You see a {item}")
    print("-" * 54)

def main():
    # Dictionary linking rooms to one another and linking items to their rooms
    rooms = {
        'Main Garage': {
            'north': 'Parts Storage Room',
            'south': 'Fab Shop / Welding Bay',
            'east': 'Tool Shed',
            'west': 'Pit Lane'
        },
        'Parts Storage Room': {
            'south': 'Main Garage',
            'item': 'High-Flow Carburetor'
        },
        'Fab Shop / Welding Bay': {
            'north': 'Main Garage',
            'item': 'Upgraded Roll Cage'
        },
        'Tool Shed': {
            'west': 'Main Garage',
            'item': 'Fire Extinguisher'
        },
        'Pit Lane': {
            'east': 'Main Garage',
            'north': 'Trailer Staging',
            'item': 'Dual-Port Intake Manifold'
        },
        'Trailer Staging': {
            'south': 'Pit Lane',
            'east': 'Overflow Yard',
            'item': '35-Inch Regulated Tires'
        },
        'Overflow Yard': {
            'west': 'Trailer Staging',
            'east': 'Starting Line', # Leads to villain room
            'item': '4-Point Safety Harness'
        },
        'Starting Line': {
            'west': 'Overflow Yard',
            'item': 'Bounty Hill Official' # Villain room ends the game
        }
    }

    # Set initial game state
    current_room = 'Main Garage'
    inventory = []
    total_items_needed = 6  # Total performance/safety upgrades required to win

    # Show instructions at the start of the game
    show_instructions()

    # Main gameplay loop
    while True:
        # Display current status and prompt for player command
        show_status(current_room, inventory, rooms)
        
        move = input("Enter your move: ").strip().lower()
        move_list = move.split()

        # Handle exiting the game
        if move == 'exit':
            print("\nExiting game. Good luck tuning your sand rail!")
            break

        # Handle movement commands (e.g., 'go north')
        elif len(move_list) == 2 and move_list[0] == 'go':
            direction = move_list[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                
                # Check if the player entered the villain room (Starting Line)
                if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Bounty Hill Official':
                    print(f"\nYou rolled up to the {current_room} and faced the {rooms[current_room]['item']} unprepared!")
                    print("Tech inspection failed! You missed vital upgrades and can't climb the hill. GAME OVER!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break
            else:
                print("\nInvalid direction! You can't go that way from here.")

        # Handle getting items (e.g., 'get high-flow carburetor')
        elif len(move_list) >= 2 and move_list[0] == 'get':
            # Reconstruct item name with proper title capitalization
            item_name = " ".join(move_list[1:]).title()
            
            # Check if room has an item and it matches the requested item
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == item_name:
                if item_name not in inventory:
                    inventory.append(item_name)
                    print(f"\nYou loaded up the {item_name} into your rig!")
                    
                    # Check win condition: player has collected all 6 required items
                    if len(inventory) == total_items_needed:
                        print("\nCongratulations! You have collected all 6 upgrades and conquered Bounty Hill!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        break
                else:
                    print(f"\nYou already packed the {item_name}.")
            else:
                print(f"\nThere is no {item_name} here to grab.")

        # Handle invalid inputs
        else:
            print("\nInvalid command! Please use 'go [direction]' or 'get [item name]'.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
