import random
from termcolor import colored

# . -> empty space (ghosts and pacman can walk)
# | and - -> wall, no one can go through it
# @ -> our hero: Pacman
# G -> ghosts, they are the bad folks
# P -> pills. Pacman needs to eat them
map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

ui_wall = [
	"......",
	"......",
	"......",
	"......"
]

ui_ghost = [
	" .-.  ",
	"| OO| ",
	"|   | ",
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

wall_color = "blue"
ghost_color = "red"
pacman_color = "yellow"
pill_color = "grey"

game_finished = False
win = False
while not game_finished:
    for row in map:
        for piece in range(4):
            for point in row:
                if point == 'G':
                    print(colored(ui_ghost[piece], ghost_color), end='')
                elif point == '|' or point == '-':
                    print(colored(ui_wall[piece], wall_color), end='')
                elif point == '@':
                    print(colored(ui_hero[piece], pacman_color), end='')
                elif point == '.':
                    print(ui_empty[piece], end='')
                elif point == 'P':
                    print(colored(ui_pill[piece], pill_color), end='')

            print("", end='\n')

    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x, y])

    for ghost in all_ghosts:
        old_ghost_x = ghost[0]
        old_ghost_y = ghost[1]

        possible_directions = [
            [old_ghost_x, old_ghost_y + 1],  
            [old_ghost_x + 1, old_ghost_y],  
            [old_ghost_x, old_ghost_y - 1],  
            [old_ghost_x - 1, old_ghost_y]
        ]

        random_movement = random.randint(0,2)
        next_ghost_x = possible_directions[random_movement][0]
        next_ghost_y = possible_directions[random_movement][1]

        y_is_valid = next_ghost_y >= 0 and next_ghost_y <= len(map[0])
        x_is_valid = next_ghost_x >= 0 and next_ghost_x < len(map)

        if not (y_is_valid and x_is_valid):
            continue

        is_wall = map[next_ghost_x][next_ghost_y] == '|' or map[next_ghost_x][next_ghost_y] == '-'
        is_ghost = map[next_ghost_x][next_ghost_y] == 'G'
        is_pill = map[next_ghost_x][next_ghost_y] == 'P'
        is_pacman = map[next_ghost_x][next_ghost_y] == '@'

        if not is_wall and not is_ghost:
            if is_pacman:
                game_finished = True
            else:
                map[old_ghost_x] = map[old_ghost_x][0:old_ghost_y] + "." + map[old_ghost_x][old_ghost_y + 1:]
                map[next_ghost_x] = map[next_ghost_x][0:next_ghost_y] + "G" + map[next_ghost_x][next_ghost_y + 1:]

    if game_finished:
        break

    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    next_pacman_x = pacman_x
    next_pacman_y = pacman_y

    key = input()

    if key == 'a':
        next_pacman_y-=1
    elif key == 's':
        next_pacman_x += 1
    elif key == 'w':
        next_pacman_x-=1
    elif key == 'd':
        next_pacman_y += 1
    else:
        continue

    y_is_valid = next_pacman_y >= 0 and next_pacman_y <= len(map[0])
    x_is_valid = next_pacman_x >= 0 and next_pacman_x <= len(map)
    if not (x_is_valid and y_is_valid):
        continue

    is_wall = map[next_pacman_x][next_pacman_y] == '|' or map[next_pacman_x][next_pacman_y] == '-'
    if is_wall:
        continue

    is_ghost = map[next_pacman_x][next_pacman_y] == 'G'
    if is_ghost:
        game_finished = True
        win = False

    map[pacman_x] = map[pacman_x][0:pacman_y] + "." + map[pacman_x][pacman_y+1:]
    map[next_pacman_x] = map[next_pacman_x][0:next_pacman_y] + "@" + map[next_pacman_x][next_pacman_y + 1:]

    total_pills = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total_pills += 1

    if total_pills <= 2:
        win = True
        game_finished = True
        break

final_board_color = "red" if win else "green"

for row in map:
    for piece in range(4):
        for point in row:
            if point == 'G':
                print(colored(ui_ghost[piece], final_board_color), end='')
            elif point == '|' or point == '-':
                print(colored(ui_wall[piece], final_board_color), end='')
            elif point == '@':
                print(colored(ui_hero[piece], final_board_color), end='')
            elif point == '.':
                print(colored(ui_empty[piece], final_board_color), end='')
            elif point == 'P':
                print(colored(ui_pill[piece], final_board_color), end='')

        print("", end='\n')

if win:
    print("You lose! :)")
else:
    print("You win! :/")