import re


def using_regex():
    with open("input.txt", "r") as file:
        ranges = next(file).split(",")
        print(ranges)

        # Same as the one in part 1 but now the "+" makes it so
        # we're trying to match the substring multiple times over the string
        regex = re.compile(
            r"^(\d+)\1+$"
        )  # start of string, capture: digit, 1 or more; that pattern, 1 or more, at the end
        print(regex)

        acc = 0
        for r in ranges:
            begin, end = map(int, r.split("-"))

            for i in range(begin, end + 1):
                if i < 10:
                    continue

                if regex.match(str(i)):
                    acc += i

        print(acc)


using_regex()
