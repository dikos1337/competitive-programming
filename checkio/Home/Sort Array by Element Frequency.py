from collections import Counter


def frequency_sort(items: list):
    # your code here
    c = Counter(items)
    if len(items) == 0:
        return items
    print(c.most_common())
    if c.most_common()[0][1] == 1:
        return items
    answer = sorted(
        items, key=lambda x: (items.count(x), -items.index(x)), reverse=True
    )
    print(answer)
    return answer


if __name__ == "__main__":
    print("Example:")
    # print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing

    assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
        "bob",
        "bob",
        "bob",
        "carl",
        "alex",
    ]
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([1, 2, 2, 1])) == [1, 1, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    print("Coding complete? Click 'Check' to earn cool rewards!")
