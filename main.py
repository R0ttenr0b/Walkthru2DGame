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
    current_image = images[play_pos[0]][play_pos[1]]
    next_image_pos = current_image["next"].get(directiuon)
    if next_image_pos is not None:
        next_image = images[next_image_pos[0]][play_pos[1]]
        current_image_index = images.index(next_image)
        return current_image_index
    
#display the images
def display_image():
    current_image = images[current_image_index]
     filename = current_image["filename"]
  image_path = os.path.join("images", filename)
    # display image here
    print("Displaying image:", image_path)

# loop for user input and image display
while True:
    # get user input
    direction = input("move (left,up, right, down):")
    # get next image index based on user input
    current_image_index = get_next_image_index(direction)
    # display current image
    display_image()

        
