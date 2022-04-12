with open("sample.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]

i = file.index("")

insertion_rules = {}
for line in file[i + 1 :]:
    from_, to_ = line.split(" -> ")
    insertion_rules[from_] = to_

# template = file[0]
template = {}
for i in range(len(file[0]) - 1):
    polymer = file[0][i] + file[0][i + 1]
    if polymer in template:
        template[polymer] += 1
    else:
        template[polymer] = 1

    # pass
print(f"{template=}")
print(insertion_rules)


def step(template: dict[str, int]):
    new_template = template.copy()

    for k, v in template.items():
        # print(f"{k=}")
        a, b = k[0], k[1]
        polymer = a + insertion_rules[k]
        if polymer in template:
            new_template[polymer] += v
        else:
            new_template[polymer] = v

    return new_template


for i in range(10):
    # print("i =", i)
    template = step(template)
    # print(f"{template = }")


cnt = {}
for k, v in template.items():
    for char in k:
        if char in cnt:
            cnt[char] += v
        else:
            cnt[char] = v


print(f"{template = }")
template_sum = sum(template.values()) + 1
print(f"{template_sum=}")


print(f"{cnt=}")
answer = max(cnt.values()) - min(cnt.values())
print(f"{answer = }")
