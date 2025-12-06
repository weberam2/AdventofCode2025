# Damnit, what I tried originally was too memory intensive, so I ended up asking Claude
ranges = []
avail_ids = []
ids = False
with open("Input.txt", "r") as file:
    content = (
        file.read().strip().split("\n\n")
    )  # split where there is two \n in a row (a blank line between text in this case)
    ranges = content[0].split("\n")  # the first block of text

print(ranges)

all_ing_ids = []
for item in ranges:
    print(item)
    start, end = map(
        int, item.split("-")
    )  # I need to learn more about python's 'map' function
    all_ing_ids.append([start, end])
"""
map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator).
It is a higher-order function used for uniform element-wise transformations, enabling concise and efficient code.
"""
all_ing_ids = sorted(all_ing_ids)
print(all_ing_ids)

"""
Ok, basically what the following does is looks for if the lower number exists in another later set (ordered), and if it does, it is replaced with the lower number
Then it does it again with the bigger numbers
"""
count = 0
for ranges in all_ing_ids:
    print(ranges)
    first, last = ranges[0], ranges[1]
    print(first)
    for start, end in all_ing_ids:
        if (start, end) != tuple(ranges) and start <= first <= end:
            print(f"Id exists! between {start} and {end}")
            all_ing_ids[count][0] = start
            break
    print(all_ing_ids)
    count += 1
count = 0
for ranges in all_ing_ids:
    print(ranges)
    first, last = ranges[0], ranges[1]
    print(last)
    for start, end in sorted(all_ing_ids, key=lambda x: x[1], reverse=True):
        if (start, end) != tuple(ranges) and start <= last <= end:
            print(f"Id exists! between {start} and {end}")
            all_ing_ids[count][1] = end
            break
    print(all_ing_ids)
    count += 1

print(all_ing_ids)
# convert to tuple, makes a set (unique), then converts back to list
unique = list(set(tuple(x) for x in all_ing_ids))
unique = [list(x) for x in unique]
print(unique)

# just count the difference and sum!
finalsum = 0
for i in unique:
    print(i)
    finalsum += int(i[1]) - int(i[0]) + 1

print(finalsum)
