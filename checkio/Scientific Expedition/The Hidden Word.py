def checkio(text: str, word: str) -> list[int]:
    # step 1 : text to matrices
    search_range = len(word)
    text = text.replace(" ", "").lower().split("\n")
    horizontal_lenghts = {i: len(t) for i, t in enumerate(text)}
    max_lenght = max(horizontal_lenghts.values())

    matrix = [list(x) for x in text]

    # Выравнивание сторон
    for i in range(len(matrix)):
        if len(matrix[i]) < max_lenght:
            diff = max_lenght - len(matrix[i])
            for j in range(diff):
                matrix[i].append("-")

    for m in matrix:
        print(m)

    print(horizontal_lenghts)
    print(max_lenght)
    # step 2 : Скользящим окном размера len(world) искать слово по горизонтали и вертикали
    if len(word) <= len(matrix):
        # горизонталь
        for row in range(len(matrix)):
            for col in range(max_lenght - search_range):
                subtext = "".join(matrix[row][col : col + search_range])
                print(subtext)
                if subtext == word:
                    return [row + 1, col + 1, row + 1, col + search_range]

    print("---" * 20)
    # вертикаль
    r = len(matrix) - (search_range)
    print("R", r)

    for row in range(r+1):
        for col in range(max_lenght):
            # print("ROW:", row, "COL:", col)
            subtext = []

            for x in range(search_range):
                subtext.append(matrix[row + x][col])
                print("append")

            subtext = "".join(subtext)
            print(subtext)

            if subtext == word:
                print("MATCH!")
                print([row + 1, col + 1, row + search_range, col + 1])
                return [row + 1, col + 1, row + search_range, col + 1]

    print("len(matrix)", len(matrix))
    return None


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
            checkio(
                """DREAMING of apples on a wall,
    And dreaming often, dear,
    I dreamed that, if I counted all,
    -How many would appear?""",
                "ten",
            )
            == [2, 14, 2, 16]
        )
    assert (
            checkio(
                """He took his vorpal sword in hand:
    Long time the manxome foe he sought--
    So rested he by the Tumtum tree,
    And stood awhile in thought.
    And as in uffish thought he stood,
    The Jabberwock, with eyes of flame,
    Came whiffling through the tulgey wood,
    And burbled as it came!""",
                "noir",
            )
            == [4, 16, 7, 16]
        )

    assert (
        checkio(
            """Twas brillig, and the slithy toves
    Did gyre and gimble in the wabe;
    All mimsy were the borogoves,
    And the mome raths outgrabe.""",
            "stog",
        )
        == [1, 19, 4, 19]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
