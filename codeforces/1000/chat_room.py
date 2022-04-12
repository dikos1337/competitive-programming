def check(string):

    word = ""

    for s in string:
        if s == "h" and word.count("h") < 1:
            word += s
            continue
        if s == "e" and word.count("e") < 1 and word.count("h") == 1:
            word += s
            continue
        if s == "l" and word.count("l") < 1 and word.count("e") == 1:
            word += s
            continue
        if s == "l" and word.count("l") < 2 and word.count("l") == 1:
            word += s
            continue
        if s == "o" and word.count("o") < 1 and word.count("l") == 2:
            word += s
            continue

    # print(word, string)
    if word == "hello":
        return "YES"
    else:
        return "NO"


# assert check("helhcludoo") == "YES"
# assert check("hehwelloho") == "YES"
# assert check("ahhellllloou") == "YES"
# assert check("hlelo") == "NO"
# assert check("pnnepelqomhhheollvlo") == "YES"

s = input()
print(check(s))
