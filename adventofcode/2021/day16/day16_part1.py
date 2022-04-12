with open("sample.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]


def hex_to_bin(num: str) -> str:
    return "%04d" % int(bin(int(num, 16))[2:])


def type_4_decode(packet: str):
    groups = []
    for i in range(0, len(packet), 5):
        groups.append(packet[i : i + 5][1:])

    groups = list(filter(lambda x: len(x) > 3, groups))
    return int("".join(groups), 2)


# packet = file[0]
packet_hex = "38006F45291200"
# for n in packet_hex:
#     print(hex_to_bin(n))

print(f"{packet_hex = }")
packet_bin = "".join([hex_to_bin(x) for x in packet_hex])
print(f"{packet_bin = }")

packet_version = int(packet_bin[:3], 2)
print(f"{packet_version = }")
packet_type_id = int(packet_bin[3:6], 2)
print(f"{packet_type_id = }")


if packet_type_id == 4:
    print(type_4_decode(packet_bin[6:]))
else:
    length_type_id = int(packet_bin[6])
    print(f"{length_type_id = }")
    message_lenght = 15 if length_type_id == 0 else 11
    print(f"{message_lenght = }")
    if message_lenght == 15:
        length_of_the_sub_packets = packet_bin[7 : 7 + message_lenght]
        print(f"{length_of_the_sub_packets = }")
    if message_lenght == 11:
        raise NotImplementedError
