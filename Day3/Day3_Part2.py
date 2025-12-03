import numpy as np
import re

maxnum_array = []
numdigits = 12
indexarray = []


def Battery():
    with open("Input.txt", "r") as file:
        for line in file:
            line = line.strip()  # remove \n from end
            print(line)
            # first number
            newstart = 0
            maxnum = []
            for d in reversed(range(numdigits)):  # 1,0
                if d == 0:
                    last = None
                else:
                    last = -d
                print(f"starting loop {numdigits - d}")
                for i in reversed(range(1, 10)):  # 9,8,7...,1
                    index = re.search(str(i), line[newstart:last])
                    print(line[newstart:last])
                    print(index)
                    if index != None:
                        number = line[newstart:last][int(index.start())]
                        print(f"number is {int(number)}")
                        maxnum.append(number)
                        newstart = newstart + int(index.start()) + 1
                        print(f"newstart is {newstart}")
                        break
            maxnum_array.append("".join(maxnum))


Battery()
print(sum(list(map(int, maxnum_array))))
