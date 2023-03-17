import os
import json



# where the player is starting 
play_pos = [0,0]

#making a 5x5 map
map = [
    [(1,0), (0, 0), (0, 0), (0, 0), (0, 2)],
    [(0,0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0,0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0,0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(3,0), (0, 0), (0, 0), (0, 0), (0, 4)], ]
 
# where the player is starting 
play_pos = [0,0]   

#images
with open("2dpics.json","r")as f:
    images_data = json.load(f)
    images = images_data["images"]

#move function
def move(direction):
    global play_pos

    new_pos = play_pos.copy()
    if direction == "left":
        new_pos [1] -= 1
    elif direction == "right":
        new_pos [1] += 1
    elif direction == "up":
        new_pos [0] -= 1
    elif direction == "down":
        new_pos [0] += 1

    if 0 <= new_pos[0] < len(map) and 0 <= new_pos[1] < len(map[0]):
        tile = map[new_pos[0]][new_pos[1]]
        if tile != (0, 0):
            play_pos = new_pos

#get the user to move
direction = input("move (left,up, right, down):")

move(direction)
# display game map with player position
for i, row in enumerate(map):
    for j, tile in enumerate(row):
        if (i, j) == tuple(play_pos):
            # display player image
            print(images['player'], end=' ')
        elif tile == (0, 0):
            # display empty tile image
            print(images['empty'], end=' ')
        elif tile == (1, 0):
            # display left wall image
            print(images['left_wall'], end=' ')
        elif tile == (2, 0):
            # display right wall image
            print(images['right_wall'], end=' ')
        elif tile == (3, 0):
            # display top wall image
            print(images['top_wall'], end=' ')
        elif tile == (4, 0):
            # display bottom wall image
            print(images['bottom_wall'], end=' ')
    print()