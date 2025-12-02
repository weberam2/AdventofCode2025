import math

dial_start = 50
old_number = dial_start
password = 0
timeszero = 0


def read_dial(instructions):
    direction = instructions[0]
    number = int(instructions[1:])
    if direction == "L":
        direction_print = "Left"
        number = number * -1
    else:
        direction_print = "Right"

    return number, direction_print


with open("input_simple.txt", "r") as file:
    for line in file:
        # print(line.strip())

        number, direction_print = read_dial(line.strip())

        if abs(number) > 99:
            password += math.floor(abs(number) / 100)
            if number > 0:
                number = number % 100
            else:
                number = -(abs(number) % 100)

        new_number = old_number + number
        if new_number < 0:
            new_number += 100
            if old_number != 0:
                password += 1
        if new_number > 99:
            new_number -= 100
            if new_number != 0:
                password += 1

        if new_number == 0:
            password += 1
        print(
            f"starting from {old_number}, dial will move {direction_print} {number} times\n"
            f"new number is {new_number}\n"
            f"new password is {password}"
        )
        old_number = new_number

print(f"password is {password}")
