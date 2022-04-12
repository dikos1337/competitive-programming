def is_acceptable_password(password: str) -> bool:
    if len(password) < 6:
        return False

    digit_check = False

    for p in password:
        if p.isdigit():
            digit_check = True

    return digit_check


if __name__ == "__main__":
    print("Example:")
    print(is_acceptable_password("short"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")