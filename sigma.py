import random

# Constants
GRID_SIZE = 9
MAX_MOVES = 80

# Function to initialize the grid and game state
def initialize_game():
    player_position = [1, 1]  # Player starts at (1, 1)
    bombs = []  # List to store bomb coordinates
    moves = 0  # Tracks the number of moves
    return player_position, bombs, moves

# Function to check if the player's position is on a bomb
def check_bomb(player_position, bombs):
    return player_position in bombs

# Function to display the game state
def display_game_state(player_position, bombs, moves):
    print(f"Current Position: {player_position}")
    print(f"Bombs: {bombs}")
    print(f"Moves Left: {MAX_MOVES - moves}")
    print("-" * 20)

# Function to run the game loop
def play_game():
    player_position, bombs, moves = initialize_game()

    while moves < MAX_MOVES:
        # Display the current state
        display_game_state(player_position, bombs, moves)

        # Get the player's next move (coordinates)
        try:
            x, y = map(int, input("Enter your next move (x, y) separated by a space: ").split())
            if x < 1 or x > GRID_SIZE or y < 1 or y > GRID_SIZE:
                print("Invalid coordinates. Please enter coordinates between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers separated by a space.")
            continue

        # Update the player's position
        player_position = [x, y]

        # Check if the player has stepped on a bomb
        if check_bomb(player_position, bombs):
            print("ChiBaBom! You stepped on a bomb. Game Over!")
            break

        # Add a new bomb at a random location
        bomb = [random.randint(1, GRID_SIZE), random.randint(1, GRID_SIZE)]
        bombs.append(bomb)

        # Increment the move count
        moves += 1

    if moves == MAX_MOVES:
        print("Good Job Skibidi Sigma Ohio! You survived the game!")

# Start the game
play_game()
