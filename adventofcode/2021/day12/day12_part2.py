from collections import defaultdict

with open("/home/dikos/code/adventofcode/2021/day12/input.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]


graph = defaultdict(list)

for line in file:
    a, b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)


for k, v in graph.items():
    print(f"{k=} : {v=}")


def check_condition(node: str, current_path: list[str]) -> bool:
    if node.isupper():
        return True

    current_path_lower = list(filter(lambda x: x.islower(), current_path))
    if node in current_path_lower:
        if node == "start":
            return False
        if node == "end":
            return False

        cnt = {k: current_path_lower.count(k) for k in current_path_lower}
        if sum(cnt.values()) >= len(set(current_path_lower)) + 1:
            return False
        else:
            return True

    return True


def search(
    graph: defaultdict[str, list[str]],
    start_node: str = "start",
    current_path: list[str] = [],
    visited_paths: set[tuple[str]] = set(),
):
    current_path.append(start_node)
    if start_node == "end":
        visited_paths.add(tuple(current_path))

    for node in graph[start_node]:
        if check_condition(node, current_path):
            visited_paths |= search(graph, node, current_path, visited_paths)
            current_path.pop()

    return visited_paths


paths = search(graph)
for path in paths:
    print(path)

print(len(paths))
