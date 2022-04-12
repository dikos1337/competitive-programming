with open("input.txt", "r") as f:
    # with open("sample.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]

i = file.index("")

insertion_rules = {}
for line in file[i + 1 :]:
    from_, to_ = line.split(" -> ")
    insertion_rules[from_] = to_

template = file[0]

print(insertion_rules)


def step(template):
    new_template = []

    for i in range(len(template) - 1):
        polymer = template[i] + template[i + 1]
        new_template.append(template[i])
        new_template.append(insertion_rules[polymer])
    new_template.append(template[-1])
    return "".join(new_template)


print(f"{template = }")

for _ in range(10):
    template = step(template)
    print(f"{template = }")


cnt = {}
for char in template:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1

print(len(template))
answer = max(cnt.values()) - min(cnt.values())
print(f"{answer = }")
