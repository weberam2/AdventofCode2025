from primePy import primes
import numpy as np

with open("./input.txt", "r") as file:
    for line in file:
        puzzle_input = line.strip()

# print(puzzle_input)

puzzle_list = puzzle_input.split(",")


# Source - https://stackoverflow.com/a
# Posted by rlms, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-02, License - CC BY-SA 3.0
def chunkstring(string, length):
    chunks = len(string) // length
    return (string[0 + i : chunks + i] for i in range(0, len(string), chunks))


def invalid_pattern(pattern, sum_invid):
    length = len(str(pattern))
    prime_factors = np.unique(primes.factors(length))
    # print(prime_factors)
    if (
        length != 1
    ):  # whoops! was getting the wrong answer because a single number was counting as repeated
        if len(set(str(pattern))) == 1:
            # print("number is repeating patterns")
            sum_invid.append(pattern)
        else:
            for factor in prime_factors:
                if length != factor:
                    if len(set(list(chunkstring(str(pattern), factor)))) == 1:
                        # print("invalid pattern found!")
                        sum_invid.append(pattern)
    return sum_invid


sum_invid = []
for row in range(len(puzzle_list)):
    item = puzzle_list[row]
    # print(item)
    dash = "-"
    dashindex = item.index(dash)
    start = int(item[0:dashindex])
    end = int(item[dashindex + 1 :])
    for num in range(start, end + 1):
        # print(num)
        sum_invid = invalid_pattern(num, sum_invid)
        # print(f"sum_invid is {sum_invid}")

print(sum_invid)
print(np.sum(sum_invid))
print(np.sum(np.unique(sum_invid)))
