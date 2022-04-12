from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    string_sum: list[str] = []
    num_sum = 0

    for item in items:
        if isinstance(item, str):
            string_sum.append(item)
        else:
            num_sum += item

    return ("".join(string_sum), num_sum)


if __name__ == "__main__":
    print("Example:")   
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
