with open("day3.txt", "r") as f:
    map_ = f.read().split("\n")


map_lenght = len(map_[0])
map_height = len(map_)

rules = {"right": 3, "down": 1}

x = 0
y = 0

counter = 0

while y != map_height:
    print("y =", y, "x =", x, "map = ", map_[y][x])

    if map_[y][x] == "#":
        counter += 1

    x += rules["right"]
    y += rules["down"]

    if x >= map_lenght:
        print("overlap")
        x -= map_lenght

print(counter)
