def check(s: str):
    output: str = ""

    for c in s:
        if c == "H":
            output += "H"
        if c == "Q":
            output += "Q"
        if c == "9":
            output += "9"

    if output != "":
        return "YES"
    else:
        return "NO"


# assert check("Hi!") == "YES"
# assert check("Codeforces") == "NO"

s = input()
print(check(s))
