def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    start_index = word.find(first)
    second_index = word.find(second)
    print(start_index)
    if start_index == -1:
        return False

    if start_index + 1 == len(word):
        return False

    if start_index > second_index:
        return False
    
    print("word[start_index + 1]",word[start_index + 1], second)
    print(word,word[start_index + 1] == second)
    return word[start_index + 1] == second


if __name__ == "__main__":
    print("Example:")
    print(goes_after("world", "w", "o"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("almaz", "m", "a") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
