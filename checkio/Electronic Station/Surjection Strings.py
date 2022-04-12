def isometric_strings(str1: str, str2: str) -> bool:

    z = list(zip(str1, str2))
    # print(z)
    d = {}
    # your code here
    for pair in z:
        v1, v2 = pair
        if v1 not in d.keys():
            d.update({v1: v2})
        else:
            if v2 == d[v1]:
                continue
            else:
                return False
    # print(d)

    return True


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
