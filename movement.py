pla_x = 1
pla_y = 1
pla_dir = 'up'
# where the player is starting 

#making a 5x5 map
map = [
    [1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1]
]
#images
images =[]
for i in range(32):

#move function
def move(direction):
    global pla_pos

    new_pos = pla_pos.copy()
    if direction == "left":
        new_pos [1] =- 1

