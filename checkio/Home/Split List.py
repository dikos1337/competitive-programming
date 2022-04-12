def split_list(items: list) -> list:
    i = len(items) // 2
    offset = 0 if len(items) % 2 == 0 else 1
    print(i, len(items), offset)
    # your code here
    answer = [items[: i + offset], items[i + offset :]]
    print(answer)
    return answer


if __name__ == "__main__":
    print("Example:")
    # print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
