def safe_pawns(pawns: set) -> int:
    chars = ["a", "b", "c", "d", "e", "f", "g", "h"]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    map_ = {c: n for c, n in zip(chars, nums)}
    reverse_map = {n: c for c, n in zip(chars, nums)}
    already_counted = []
    counter = 0
    print(map_)
    print(reverse_map)

    def top_left_exists(p: str) -> bool:
        c = p[0]
        n = int(p[1])
        top_left_pos_char = reverse_map.get(map_.get(c, 0) - 1)
        top_left_pos_num = n + 1
        if top_left_pos_num > 8:
            return False
        if not top_left_pos_char:
            return False
        top_left_pos = f"{top_left_pos_char}{top_left_pos_num}"

        print(f"p:{p} , top_left_pos: {top_left_pos}")
        answer = (top_left_pos in pawns) and (top_left_pos not in already_counted)
        print("answer top_left_pos", answer)
        if answer:
            already_counted.append(top_left_pos)
        return answer

    def top_right_exists(p: str) -> bool:
        c = p[0]
        n = int(p[1])
        top_right_pos_char = reverse_map.get(map_.get(c, 0) + 1)
        top_right_pos_num = n + 1
        if top_right_pos_num < 1:
            return False
        if not top_right_pos_char:
            return False
        top_right_pos = f"{top_right_pos_char}{top_right_pos_num}"

        print(f"p:{p} , top_right_pos: {top_right_pos}")
        answer = (top_right_pos in pawns) and (top_right_pos not in already_counted)
        print("answer top_right_pos", answer)
        if answer:
            already_counted.append(top_right_pos)
        return answer

    for pawn in pawns:

        p_top_left_exists = top_left_exists(pawn)
        p_top_right_exists = top_right_exists(pawn)
        counter += sum([p_top_left_exists, p_top_right_exists])

    print(counter)
    return counter  # - 1 if counter else counter


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6

    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"e4"}) == 0
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")