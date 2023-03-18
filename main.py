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
