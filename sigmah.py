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

# Function to display the grid with bombs and the player's position
def display_grid(player_position, bombs):
    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Mark the player's position on the grid
    grid[player_position[1] - 1][player_position[0] - 1] = "P"

    # Mark the bombs on the grid
    for bomb in bombs:
        grid[bomb[1] - 1][bomb[0] - 1] = "B"

    # Print the grid
    for row in grid:
        print(" ".join(row))
    print("#" * 20)

# Function to run the game loop
def play_game():
    player_position, bombs, moves = initialize_game()

    while moves < MAX_MOVES:
        # Display the grid at the start of each round
        display_grid(player_position, bombs)

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
        for _ in range(moves + 1):  # Add 1 more bomb each round
            bomb = [random.randint(1, GRID_SIZE), random.randint(1, GRID_SIZE)]
            bombs.append(bomb)

        # Increment the move count
        moves += 1

    if moves == MAX_MOVES:
        print("Good Job Skibidi Sigma Ohio! You survived the game!")

# Start the game
play_game()
