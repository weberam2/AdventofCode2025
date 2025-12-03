import numpy as np
import re

maxnum = []


def Battery():
    with open("Input.txt", "r") as file:
        for line in file:
            line = line.strip()
            # batnumber = [int(i) for i in str(line.strip())]
            print(line)
            # first number
            for i in reversed(range(10)):
                index = re.search(str(i), line[:-1])
                if index != None:
                    firstnumber = line[int(index.start())]
                    print(f"first number is {int(firstnumber)}")
                    break
            for i in reversed(range(10)):
                newline = line[int(index.start()) + 1 :]
                secindex = re.search(str(i), line[int(index.start()) + 1 :])
                # print(newline)
                if secindex != None:
                    secondnumber = newline[int(secindex.start())]
                    print(f"second number is {int(secondnumber)}")
                    break
            maxnum.append(int(firstnumber + secondnumber))


Battery()
print(sum(maxnum))
