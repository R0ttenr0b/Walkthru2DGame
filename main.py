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
with open("2dpicsM.json","r") as f:
    images_data = json.load(f)
    images = images_data.get("images", [])

current_image_index = 0

def next_image_index(directiuon):
    global current_image_index
    current_image = image[play_pos[0]][play_pos[1]]
    next_image_pos = current_image["next"].get(directiuon)
    if next_image_pos is not None:
        next_image = image[current_image]

        
