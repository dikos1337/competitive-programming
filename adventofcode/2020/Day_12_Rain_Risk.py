with open("day12.txt", "r") as f:
    input_data = f.read().split("\n")

actions = []

for command in input_data:
    action, value = command[0], int(command[1:])
    actions.append({"action": action, "value": value})

# print(*actions)

current_direction = "E"
directions = ["W", "N", "E", "S"]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"x: {self.x} y: {self.y}"

    def calculate_manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    @staticmethod
    def set_current_direction(degrees):
        global current_direction, directions
        idx = directions.index(current_direction)
        new_direction_idx = ((degrees // 90) + idx) % 4
        current_direction = directions[new_direction_idx]


class ActionInterpreter:
    def __init__(self, position: Position, action: dict):
        self.action = action["action"]
        self.value = action["value"]
        self.position = position
        self.define_action()

    def define_action(self):
        if self.action == "N":
            self.north()
        elif self.action == "S":
            self.south()
        elif self.action == "E":
            self.east()
        elif self.action == "W":
            self.west()
        elif self.action == "L":
            self.left()
        elif self.action == "R":
            self.right()
        elif self.action == "F":
            self.forward()

    def north(self):
        global current_position
        current_position = Position(self.position.x, self.position.y - self.value)

    def south(self):
        global current_position
        current_position = Position(self.position.x, self.position.y + self.value)

    def west(self):
        global current_position
        current_position = Position(self.position.x - self.value, self.position.y)

    def east(self):
        global current_position
        current_position = Position(self.position.x + self.value, self.position.y)

    def right(self):
        Position.set_current_direction(self.value)

    def left(self):
        Position.set_current_direction(-self.value)

    def forward(self):
        global current_direction
        self.action = current_direction
        self.define_action()


current_position = Position(0, 0)

for action in actions:
    ActionInterpreter(current_position, action)
    print(current_position)

print("answer", current_position.calculate_manhattan_distance())
