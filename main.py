import os
import json

# where the player is starting 
play_pos = [0,0]

#making a 5x5 map
map = [
    [(1,0), 1, 1, 1, 1],
    [(0,0), 1, 1, 1],
    [(0,0), 1, 1, 1],
    [(0,0), 1, 1, 1],
    [(3,0), 1, 1, 1]
]
#images
images =[]
for i in range(32):

#move function
def move(direction):
    global pla_x,pla_y

    new_pos = pla_dir.copy()
    if direction == "left":
        new_pos [1] =- 1
    if direction == "right":
        new_pos [1] =+ 1
    if direction == "up":
        new_pos [1] =- 1
    if direction == "down":
        new_pos [1] =- 1

#get the user to move
direction = input("move (left,up, right, down);")

move(direction)


while True:
 print("Player position:",pla_y,pla_x)
 