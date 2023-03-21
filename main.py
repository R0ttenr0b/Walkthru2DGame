import os
import json

# define map
map = [
    [(1, 0), (0, 0), (0, 0), (0, 0), (0, 2)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(3, 0), (0, 0), (0, 0), (0, 0), (0, 4)]
]

# define images
with open("2dpics.json", "r") as f:
    images_data = json.load(f)
    images = images_data.get("images", [])

# define player starting position and current image
play_pos = [0, 0]
current_image = images[play_pos[0]][play_pos[1]]["front"]

# define function to get next image index
def next_image_index(direction):
    global current_image
    global play_pos
    current_position = images[play_pos[0]][play_pos[1]]
    next_position = current_position.get(direction)
    if next_position is not None:
        next_position_x, next_position_y = next_position
        next_position_image = images[next_position_x][next_position_y]
        current_image = next_position_image["front"]
        play_pos = next_position
        return current_image

# define function to display current image
def display_image():
    current_position = images[play_pos[0]][play_pos[1]]
    filename = current_position["front"]
    image_path = os.path.join("images", filename)
    # display image here
    print("Displaying image:", image_path)

# loop for user input and image display
while True:
    # get user input
    direction = input("move (left,up, right, down):")
    # get next image index based on user input
    next_image = next_image_index(direction)
    if next_image is None:
        print("Cannot move in that direction")
    else:
        # display current image
        display_image()
