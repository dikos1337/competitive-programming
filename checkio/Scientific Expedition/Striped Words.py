import re


def checkio(line: str) -> int:
    line = re.sub(r"\S*\d+\S*", " ", line)
    line = re.sub(r"[^a-zA-z]", " ", line).lower()
    words = line.split(" ")
    words = list(filter(lambda x: len(x) > 1, words))
    vowels = set("A E I O U Y".lower().split(" "))
    # consonants = "B C D F G H J K L M N P Q R S T V W X Z".lower().split(" ")
    counter = 0

    def is_vowel(char) -> bool:
        return True if char in vowels else False

    bool_words = []

    for word in words:
        # print("words", words)
        bool_word = []
        for char in word:
            bool_word.append(is_vowel(char))
        bool_words.append(bool_word)

    # print("bool_words", bool_words)

    for bword in bool_words:
        # print("bword", bword)
        bword_check: list[bool] = []

        for i, b in enumerate(bword[:-1]):
            bword_check.append(True) if b != bword[i + 1] else bword_check.append(False)
        if all(bword_check):
            # print(bword)
            counter += 1
    # print("counter", counter)
    return counter


if __name__ == "__main__":
    print("Example:")
    print(checkio("My name is ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("My name is ...") == 3
    assert checkio("Hello world") == 0
    assert checkio("A quantity of striped words.") == 1
    assert checkio("Dog,cat,mouse,bird.Human.") == 3
    assert checkio("1st 2a ab3er root rate") == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
