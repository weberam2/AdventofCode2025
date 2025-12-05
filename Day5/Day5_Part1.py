# Damnit, what I tried originally was too memory intensive, so I ended up asking Claude
ranges = []
avail_ids = []
ids = False
with open("Input.txt", "r") as file:
    content = (
        file.read().strip().split("\n\n")
    )  # split where there is two \n in a row (a blank line between text in this case)
    ranges = content[0].split("\n")  # the first block of text
    avail_ids = content[1].split("\n")  # the second block

print(ranges)

all_ing_ids = []
for item in ranges:
    print(item)
    start, end = map(
        int, item.split("-")
    )  # I need to learn more about python's 'map' function
    all_ing_ids.append((start, end))
"""
map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator).
It is a higher-order function used for uniform element-wise transformations, enabling concise and efficient code.
"""
print(all_ing_ids)

count = 0
for row in avail_ids:
    print(row)
    if any(
        start <= int(row) <= end for start, end in all_ing_ids
    ):  # this part is very cool
        print("Id exists!")
        count += 1

print(f"final count is {count}")
