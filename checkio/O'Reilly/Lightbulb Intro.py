from datetime import datetime, timedelta


def sum_light(els: list[datetime]) -> int:
    """
    how long the light bulb has been turned on
    """
    time = timedelta()

    for i in range(0, len(els), 2):
        time = time + (els[i + 1] - els[i])

    print(time.total_seconds())
    return time.total_seconds()


if __name__ == "__main__":
    # print("Example:")
    # print(
    #     sum_light(
    #         [
    #             datetime(2015, 1, 12, 10, 0, 0),
    #             datetime(2015, 1, 12, 10, 10, 10),
    #             datetime(2015, 1, 12, 11, 0, 0),
    #             datetime(2015, 1, 12, 11, 10, 10),
    #         ]
    #     )
    # )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
            ]
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
        == 1220
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 12, 10, 10),
            ]
        )
        == 4820
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 1),
            ]
        )
        == 1
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
        == 86410
    )

    print(
        "The first mission in series is completed? Click 'Check' to earn cool rewards!"
    )
