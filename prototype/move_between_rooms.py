"""Module Six Milestone: Moving Between Rooms Prototype.
Adapted for Kyle Gaston's Sand Rail Bounty Hill Game World.
"""

# A dictionary mapping rooms to adjacent rooms for movement.
# Built using the 8 rooms designed in Project One.
rooms = {
    "Main Garage": {"east": "Parts Storage Room", "west": "Fab Shop / Welding Bay", "south": "Pit Lane"},
    "Parts Storage Room": {"west": "Main Garage", "west": "Trailer Staging"}, # Matches project map connections
    "Fab Shop / Welding Bay": {"east": "Main Garage"},
    "Tool Shed": {"south": "Fab Shop / Welding Bay"}, # Connected via Fab Shop per map layout
    "Pit Lane": {"north": "Main Garage", "south": "Trailer Staging"},
    "Trailer Staging": {"north": "Pit Lane", "east": "Parts Storage Room", "west": "Overflow Yard"},
    "Overflow Yard": {"east": "Trailer Staging", "north": "Starting Line"},
    "Starting Line": {"south": "Overflow Yard"}
}

# Set the player's starting room
current_room = "Main Garage"

print("Welcome to the Sand Rail Bounty Hill Challenge!")
print("Move commands: go north, go south, go east, go west, or exit")
print("-" * 50)

# Create the gameplay loop
while current_room != "exit":
    # Display the current room
    print(f"\nYou are currently in the: {current_room}")

    # Prompt for a movement command or exit
    command = input("Enter your move: ").strip().lower()

    # Handle exit command
    if command == "exit":
        current_room = "exit"
        print("Exiting game. Good luck at the Bounty Hill!")

    # Branch for a valid movement command (e.g., 'go north')
    elif command.startswith("go "):
        direction = command.split(" ")[1]

        # Validate movement using the rooms dictionary
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way! Choose a valid direction.")

    # Input validation for invalid commands
    else:
        print("Invalid command! Please type 'go [direction]' (e.g., go north) or 'exit'.")
