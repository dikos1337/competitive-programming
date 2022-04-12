DEBUG = True

s_inp = input()

s = {i: s_inp[i] for i in range(len(s_inp)) if s_inp[i] in {"A", "B"}}
if DEBUG:
    print(s)


if len(s) < 4:
    print("NO")
    quit()

valid_keys = []
keys = list(s.keys())
for i in range(len(keys) - 1):
    if keys[i + 1] - keys[i] == 1:
        if s_inp[keys[i]] != s_inp[keys[i + 1]]:
            valid_keys.append((keys[i], keys[i + 1]))

if DEBUG:
    print("valid_keys", valid_keys)

if len(valid_keys) < 2:
    print("NO")
    quit()


# drop_indeces = set()
# for i in range(len(valid_keys) - 1):
#     k1, k2 = valid_keys[i]
#     k1, k2 = s_inp[k1], s_inp[k2]
#     t1, t2 = valid_keys[i + 1]
#     t1, t2 = s_inp[t1], s_inp[t2]
#     print(k1, k2, t1, t2)
#     if k2 == t1:
#         if k1 != t2:
#             drop_indeces.add(i + 1)

# if DEBUG:
#     print("drop_indeces", drop_indeces)

# valid_keys = [valid_keys[i] for i in range(len(valid_keys)) if i not in drop_indeces]

if DEBUG:
    print("filtered valid_keys", valid_keys)

ab = 0
ba = 0
for i in range(len(valid_keys) - 1):
    k1, k2 = valid_keys[i]


    if s_inp[k1] == "A" and s_inp[k2] == "B":
        ab += 1
    if s_inp[k1] == "B" and s_inp[k2] == "A":
        ba += 1

if DEBUG:
    print(ab, ba)

if (ab > 0) and (ba > 0):
    print("YES")
    quit()
else:
    print("NO")
    quit()
