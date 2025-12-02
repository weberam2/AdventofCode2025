with open("input.txt", "r") as file:
    for line in file:
        puzzle_input = line.strip()

print(puzzle_input)

puzzle_list = puzzle_input.split(",")


def invalid_pattern(pattern, sum_invid):
    length = len(str(pattern))
    if length % 2 == 0:
        halfway = length // 2
        start = int(str(pattern)[:halfway])
        end = int(str(pattern)[halfway:])
        print(f"start is {start}, end is {end}")
        if start == end:
            print("invalid pattern found!")
            sum_invid += pattern
    return sum_invid


sum_invid = 0
for row in range(len(puzzle_list)):
    item = puzzle_list[row]
    print(item)
    dash = "-"
    dashindex = item.index(dash)
    start = int(item[0:dashindex])
    end = int(item[dashindex + 1 :])
    for num in range(start, end + 1):
        print(num)
        sum_invid = invalid_pattern(num, sum_invid)
        print(f"sum_invid is {sum_invid}")

print(sum_invid)
