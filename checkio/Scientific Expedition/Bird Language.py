VOWELS = set("aeiouy")


def translate(phrase):
    words: list[list[str]] = [list(x) for x in phrase.split(" ")]
    print(words)
    answer: list[str] = []

    for i, word in enumerate(words):
        ans_word: list[str] = []

        word_len = len(word)
        word_char_index = 0
        while word_char_index < word_len:
            if word[word_char_index] in VOWELS:
                ans_word.append(word[word_char_index])
                word_char_index += 3
            else:
                ans_word.append(word[word_char_index])
                word_char_index += 2

        answer.append("".join(ans_word))
    
    print(answer)
    return " ".join(answer)


if __name__ == "__main__":
    # print("Example:")
    # print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
