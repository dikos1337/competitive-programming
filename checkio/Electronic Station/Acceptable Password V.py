def is_acceptable_password(password: str) -> bool:
    if len(password) < 6:
        return False

    if "password" in password.lower():
        return False

    if len(password) < 9:
        digit_check = False
        password_contains_only_digits_counter = 0

        for p in password:
            if p.isdigit():
                digit_check = True
                password_contains_only_digits_counter += 1

        if password_contains_only_digits_counter == len(password):
            return False

        return digit_check
    return True


if __name__ == "__main__":
    print("Example:")
    print(is_acceptable_password("short"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")