def yaml(a: str):
    # your code here

    lines = [line for line in a.split("\n") if line.strip() != ""]

    answer = {}
    for line in lines:
        key, value = line.split(": ")
        answer[key] = int(value) if value.isdigit() else value

    print(lines)
    print(answer)

    return answer


if __name__ == "__main__":
    #     print("Example:")
    #     print(
    #         yaml(
    #             """name: Alex
    # age: 12"""
    #         )
    #     )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        yaml(
            """name: Alex
age: 12"""
        )
        == {"age": 12, "name": "Alex"}
    )
    assert (
        yaml(
            """name: Alex Fox
age: 12

class: 12b"""
        )
        == {"age": 12, "class": "12b", "name": "Alex Fox"}
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
