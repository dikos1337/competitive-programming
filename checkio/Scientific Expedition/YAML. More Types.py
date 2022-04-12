# Taken from mission YAML. Simple Dict


def yaml(a: str):
    def decide_type(value: str):
        if value == None or value.strip() == "null" or value == "":
            return None

        value = value.strip()
        if value == "false":
            return False
        if value == "true":
            return True

        return (
            int(value)
            if value.isdigit()
            else value.removeprefix('"').removesuffix('"').replace('\\"', '"')
        )

    lines = [line for line in a.split("\n") if line.strip() != ""]

    answer = {}
    for line in lines:
        try:
            key, value = line.split(":")
        except ValueError:
            key = line.strip()
            value = None

        answer[key] = decide_type(value)

    # print(lines)
    print(answer)

    return answer


if __name__ == "__main__":
    print("Example:")
    # print(yaml("name: Alex\nage: 12"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("name: Alex\nage: 12") == {"age": 12, "name": "Alex"}
    assert yaml("name: Alex Fox\n" "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }
    assert yaml('name: "Alex Fox"\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }
    assert yaml('name: "Alex \\"Fox\\""\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": 'Alex "Fox"',
    }
    assert yaml('name: "Bob Dylan"\n' "children: 5\n" "alive: false") == {
        "alive": False,
        "children": 5,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 7\n" "coding: null") == {
        "children": 7,
        "coding": None,
        "name": "Bob Dylan",
    }
    assert yaml('name: "Bob Dylan"\n' "children: 8\n" 'coding: "null" ') == {
        "children": 8,
        "coding": "null",
        "name": "Bob Dylan",
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
