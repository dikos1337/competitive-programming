import unicodedata


def checkio(in_string):

    return "".join(
        c
        for c in unicodedata.normalize("NFD", in_string)
        if unicodedata.category(c) != "Mn"
    )


if __name__ == "__main__":

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print("Done")
