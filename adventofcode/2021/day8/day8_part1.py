with open("input.txt", "r") as f:
    file = f.readlines()


data = []
for line in file:
    data.append(line.split(" | ")[1].replace("\n", "").split(" "))


answer = 0

for signals in data:
    for signal in signals:
        if len(signal) in [2, 3, 4, 7]:
            answer += 1

print(answer)
