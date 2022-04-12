def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    print("TEXT IS:", text)

    left_index = text.find(begin)
    left_index = left_index + len(begin) if left_index >= 0 else 0
    print("left_index:", left_index)

    right_index = text.find(end)
    right_index = right_index if right_index > 0 else -len(end)
    print("right_index:", right_index)

    if right_index > 0:
        answ = text[left_index:right_index]
    else:
        answ = text[left_index:]
    print("ANSW", answ)
    return answ


if __name__ == "__main__":
    print("Example:")
    print(between_markers("What is >apple<", ">", "<"))

    # These "asserts" are used for self-checking and not for testing
    assert (
        between_markers("Never send a human to do a machine's job.", "Never", "do")
        == " send a human to "
    )
    assert between_markers("What is >apple<", ">", "<") == "apple", "One sym"
    assert (
        between_markers(
            "<head><title>My new site</title></head>", "<title>", "</title>"
        )
        == "My new site"
    ), "HTML"
    assert between_markers("No[/b] hi", "[b]", "[/b]") == "No", "No opened"
    assert between_markers("No [b]hi", "[b]", "[/b]") == "hi", "No close"
    assert between_markers("No hi", "[b]", "[/b]") == "No hi", "No markers at all"
    assert between_markers("No <hi>", ">", "<") == "", "Wrong direction"
    print("Wow, you are doing pretty good. Time to check it!")
