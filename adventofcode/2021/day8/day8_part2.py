with open("/home/dikos/code/c/adventofcode/2021/day8/input.txt", "r") as f:
    file = f.readlines()


data = []
for line in file:
    data.append(line.split(" | ")[1].replace("\n", "").split(" "))


answer = 0


def get_top_segment(seven: str, one: str) -> str:
    for char in seven:
        if char not in one:
            return char
    print("UNREACHABLE get_top_segment")


def get_right_segment(four: str, five: str) -> str:
    return list(set(list(four)) - set(list(five)))
    print("UNREACHABLE get_right_segment")


answer = []
# print("file",file)

for line in file:
    # line = "".join(
    #     [
    #         "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb ",
    #         "eafb cagedb ab | cdfeb fcadb cdfeb cdbaf",
    #     ]
    # )
    line = line.strip()
    print(f"{line=}")
    left, right = line.split(" | ")

    one_pattern = ""
    seven_pattern = ""
    four_pattern = ""
    eight_pattern = ""

    sixlen = []
    fivelen = []
    for signal in left.split(" "):
        signal = "".join(sorted(list(signal)))
        # print(len(signal), signal)
        if len(signal) == 2:
            one_pattern = signal
        elif len(signal) == 3:
            seven_pattern = signal
        elif len(signal) == 4:
            four_pattern = signal
        elif len(signal) == 7:
            eight_pattern = signal
        elif len(signal) == 5:
            fivelen.append(signal)
        elif len(signal) == 6:
            sixlen.append(signal)

    # print(f"{line = }")
    # print(f"{left = }")
    # print(f"{right = }")

    # three_pattern calc
    for signal in fivelen:
        x = "".join(list(set(signal) - set(seven_pattern)))
        # print("sig five:", signal, x)
        if len(x) == 2:
            three_pattern = signal
    # print(f"{fivecnt = }")

    left_top_segment = list(set(four_pattern) - set(three_pattern))[0]
    for signal in fivelen:  # 3 elems total
        if signal == three_pattern:
            continue
        if left_top_segment in signal:
            five_pattern = signal
            # print("5 set")
        else:
            two_pattern = signal
            # print("2 set")

    top_segment = get_top_segment(seven_pattern, one_pattern)
    # right_top_segment = get_right_segment(four_pattern, one_pattern)
    right_top_segment = list(set(list(four_pattern)) - set(list(five_pattern)))[0]
    print(f"{right_top_segment=}")
    # right_bottom_segment = list(set(one_pattern) - set([right_top_segment]))[0]
    # print(f"{top_segment = }")  # d
    # print(f"{right_top_segment = }")  # a
    # print(f"{right_bottom_segment = }")  # b

    six_pattern = "".join(sorted(list(set(list(eight_pattern)) ^ set([right_top_segment]))))

    # print(f"{left_top_segment = }")  # e

    # 9 and 0 pattern calc
    # for signal in sixlen:
    # print("sig six:", signal)
    # x = "".join(list(set(eight_pattern) - set(signal)))
    # print(x)
    # print(f"{sixcnt = }")

    for signal in sixlen:  # 3 elems total
        # print("--", six_pattern, signal)
        if sorted(list(signal)) == sorted(list(six_pattern)):
            continue
        x = "".join(list(set(signal) - set(three_pattern)))
        if len(x) == 1:
            nine_pattern = signal
        if len(x) == 2:
            zero_pattern = signal
        # print("len x -----", len(x))

    zero_pattern = "".join(sorted(list(zero_pattern)))
    one_pattern = "".join(sorted(list(one_pattern)))
    two_pattern = "".join(sorted(list(two_pattern)))
    three_pattern = "".join(sorted(list(three_pattern)))
    four_pattern = "".join(sorted(list(four_pattern)))
    five_pattern = "".join(sorted(list(five_pattern)))
    six_pattern = "".join(sorted(list(six_pattern)))
    seven_pattern = "".join(sorted(list(seven_pattern)))
    eight_pattern = "".join(sorted(list(eight_pattern)))
    nine_pattern = "".join(sorted(list(nine_pattern)))

    karta = {
        zero_pattern: "0",
        one_pattern: "1",
        two_pattern: "2",
        three_pattern: "3",
        four_pattern: "4",
        five_pattern: "5",
        six_pattern: "6",
        seven_pattern: "7",
        eight_pattern: "8",
        nine_pattern: "9",
    }

    print(f"{zero_pattern = }")
    print(f"{one_pattern = }")  # ab
    print(f"{two_pattern = }")  # gcdfa
    print(f"{three_pattern = }")  # fbcad
    print(f"{four_pattern = }")  # eafb
    print(f"{five_pattern = }")  # cdfbe
    print(f"{six_pattern = }")  # gdebcf
    print(f"{seven_pattern = }")  # dab
    print(f"{eight_pattern = }")  # acedgfb
    print(f"{nine_pattern = }")

    # print("-----")
    numstr = ""
    for signal in right.split(" "):
        sorted_signal = "".join(sorted(list(signal)))
        print(f"{sorted_signal=}")
        numstr += karta[sorted_signal]
    print(f"{numstr = }")
    answer.append(numstr)

answer = list(map(int, answer))
print(f"{answer = }", sum(answer))
