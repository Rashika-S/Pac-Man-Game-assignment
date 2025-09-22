import random
from termcolor import colored

# Constants for colors
COLOR_WALL = "blue"
COLOR_GHOST = "red"
COLOR_PACMAN = "yellow"
COLOR_PILL = "magenta"
COLOR_FINAL_WIN = "green"
COLOR_FINAL_LOSE = "red"

# UI elements
ui_wall = [
	"......",
	"......",
	"......",
	"......"
]

ui_ghost = [
	" .-.  ",
	"|> <| ",
	"| o | ",
	"'^^^' "
]

ui_hero = [
	" .--. ",
	"/ _.-'",
	"\\  '-.",
	" '--' "
]

ui_empty = [
	"      ",
	"      ",
	"      ",
	"      "
]

ui_pill = [
	"      ",
	" .-.  ",
	" '-'  ",
	"      "
]

# Create initial map
def create_map():
    return [
        "|---P....|",
        "|G..|..G.|",
        "|..P.....|",
        "|G....@|.|",
        "|...P..|.|",
        "|--------|"
    ]

# Function to print the map
def print_map(game_map, final_color=None):
    for row in game_map:
        for piece in range(4):
            for point in row:
                color = None
                if point == 'G':
                    color = COLOR_GHOST if not final_color else final_color
                    print(colored(ui_ghost[piece], color), end='')
                elif point in ['|','-']:
                    color = COLOR_WALL if not final_color else final_color
                    print(colored(ui_wall[piece], color), end='')
                elif point == '@':
                    color = COLOR_PACMAN if not final_color else final_color
                    print(colored(ui_hero[piece], color), end='')
                elif point == '.':
                    print(ui_empty[piece], end='')
                elif point == 'P':
                    color = COLOR_PILL if not final_color else final_color
                    print(colored(ui_pill[piece], color), end='')
            print()
    print()

# Function to move ghosts
def move_ghosts(game_map):
    game_finished = False
    ghosts = []
    for x, row in enumerate(game_map):
        for y, cell in enumerate(row):
            if cell == 'G':
                ghosts.append([x, y])

    for ghost in ghosts:
        old_x, old_y = ghost
        directions = [[old_x, old_y+1],[old_x+1, old_y],[old_x, old_y-1],[old_x-1, old_y]]
        nx, ny = random.choice(directions)

        if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
            target = game_map[nx][ny]
            if target == '@':
                game_finished = True
            elif target in ['.', 'P']:
                game_map[old_x] = game_map[old_x][:old_y] + "." + game_map[old_x][old_y+1:]
                game_map[nx] = game_map[nx][:ny] + "G" + game_map[nx][ny+1:]
    return game_map, game_finished

# Function to move Pacman
def move_pacman(game_map, key):
    pacman_x, pacman_y = -1, -1
    for x, row in enumerate(game_map):
        for y, cell in enumerate(row):
            if cell == '@':
                pacman_x, pacman_y = x, y

    nx, ny = pacman_x, pacman_y
    if key == 'a': ny -= 1
    elif key == 'd': ny += 1
    elif key == 'w': nx -= 1
    elif key == 's': nx += 1
    else: return game_map, False, False  # invalid key

    if not (0 <= nx < len(game_map) and 0 <= ny < len(game_map[0])): return game_map, False, False
    if game_map[nx][ny] in ['|','-']: return game_map, False, False
    if game_map[nx][ny] == 'G': return game_map, True, False

    game_map[pacman_x] = game_map[pacman_x][:pacman_y] + "." + game_map[pacman_x][pacman_y+1:]
    game_map[nx] = game_map[nx][:ny] + "@" + game_map[nx][ny+1:]

    total_pills = sum(row.count('P') for row in game_map)
    if total_pills == 0: return game_map, True, True

    return game_map, False, False

# Main game loop
def play_game():
    game_map = create_map()
    game_finished = False
    win = False

    while not game_finished:
        print_map(game_map)
        key = input("Enter move (WASD): ").lower()
        game_map, game_finished, win = move_pacman(game_map, key)
        if game_finished: break
        game_map, ghost_finished = move_ghosts(game_map)
        if ghost_finished:
            game_finished = True
            win = False

    final_color = COLOR_FINAL_WIN if win else COLOR_FINAL_LOSE
    print_map(game_map, final_color)
    print("You win! :)" if win else "You lost! :/")

# Start the game
play_game()
