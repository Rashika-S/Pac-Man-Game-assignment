import random
from termcolor import colored

# UI definitions
UI_WALL = ["......", "......", "......", "......"]
UI_GHOST = [" .-.  ", "| OO| ", "|   | ", "'^^^' "]
UI_HERO = [" .--. ", "/ _.-'", "\\  '-.", " '--' "]
UI_EMPTY = ["      ", "      ", "      ", "      "]
UI_PILL = ["      ", " .-.  ", " '-'  ", "      "]

COLOR_WALL = "blue"
COLOR_GHOST = "red"
COLOR_PACMAN = "yellow"
COLOR_PILL = "grey"
COLOR_FINAL_WIN = "green"
COLOR_FINAL_LOSE = "red"

# Pure functions for the game logic
def print_map(game_map, colors=None):
    """Prints the current game map using UI elements and colors."""
    for row in game_map:
        for piece in range(4):
            for cell in row:
                if cell == 'G':
                    color = colors['ghost'] if colors else COLOR_GHOST
                    print(colored(UI_GHOST[piece], color), end='')
                elif cell in ['|','-']:
                    color = colors['wall'] if colors else COLOR_WALL
                    print(colored(UI_WALL[piece], color), end='')
                elif cell == '@':
                    color = colors['pacman'] if colors else COLOR_PACMAN
                    print(colored(UI_HERO[piece], color), end='')
                elif cell == '.':
                    print(UI_EMPTY[piece], end='')
                elif cell == 'P':
                    color = colors['pill'] if colors else COLOR_PILL
                    print(colored(UI_PILL[piece], color), end='')
            print()
    print()

def find_positions(game_map, char):
    """Returns a list of coordinates where 'char' is found in the map."""
    positions = []
    for x, row in enumerate(game_map):
        for y, cell in enumerate(row):
            if cell == char:
                positions.append([x, y])
    return positions

def is_valid_position(game_map, x, y):
    """Checks if a position is within map bounds and not a wall."""
    if not (0 <= x < len(game_map) and 0 <= y < len(game_map[0])):
        return False
    if game_map[x][y] in ['|', '-']:
        return False
    return True

def move_ghosts(game_map):
    """Moves all ghosts randomly and returns updated map and game status."""
    ghosts = find_positions(game_map, 'G')
    game_finished = False
    new_map = game_map.copy()

    for ghost_x, ghost_y in ghosts:
        directions = [
            (ghost_x, ghost_y + 1),
            (ghost_x + 1, ghost_y),
            (ghost_x, ghost_y - 1),
            (ghost_x - 1, ghost_y)
        ]
        random.shuffle(directions)  # Randomize movement order
        for next_x, next_y in directions:
            if not is_valid_position(game_map, next_x, next_y):
                continue
            target = game_map[next_x][next_y]
            if target == 'G':
                continue
            elif target == '@':
                game_finished = True
                break
            else:
                # Move ghost
                new_row = new_map[ghost_x][:ghost_y] + '.' + new_map[ghost_x][ghost_y+1:]
                new_map[ghost_x] = new_row
                new_row = new_map[next_x][:next_y] + 'G' + new_map[next_x][next_y+1:]
                new_map[next_x] = new_row
                break
        if game_finished:
            break
    return new_map, game_finished

def move_pacman(game_map, direction):
    """Moves Pacman according to the input direction."""
    pacman_pos = find_positions(game_map, '@')[0]
    x, y = pacman_pos
    delta = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    dx, dy = delta.get(direction, (0, 0))
    next_x, next_y = x + dx, y + dy

    if not is_valid_position(game_map, next_x, next_y):
        return game_map, False, False  # invalid move

    target = game_map[next_x][next_y]
    if target == 'G':
        return game_map, True, False  # game over
    new_map = game_map.copy()
    new_map[x] = new_map[x][:y] + '.' + new_map[x][y+1:]
    new_map[next_x] = new_map[next_x][:next_y] + '@' + new_map[next_x][next_y+1:]

    total_pills = sum(row.count('P') for row in new_map)
    if total_pills == 0:
        return new_map, True, True  # win

    return new_map, False, False

def play_game(game_map):
    """Main game loop encapsulated in a function."""
    game_finished = False
    win = False
    while not game_finished:
        print_map(game_map)
        move = input("Move (WASD): ").lower()
        if move not in ['w','a','s','d']:
            continue
        game_map, game_finished, win = move_pacman(game_map, move)
        if game_finished:
            break
        game_map, ghosts_finished = move_ghosts(game_map)
        if ghosts_finished:
            game_finished = True
            win = False

    final_color = COLOR_FINAL_WIN if win else COLOR_FINAL_LOSE
    print_map(game_map, colors={'ghost': final_color, 'wall': final_color, 'pacman': final_color, 'pill': final_color})
    if win:
        print("You win! :)")
    else:
        print("You lost! :/")

# Initial map
initial_map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

# Run the game
play_game(initial_map)
