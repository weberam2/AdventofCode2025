import numpy as np

# 2D array

with open("Input.txt") as datafromfile:
    textarray = datafromfile.readlines()

textarray = [list(line.strip()) for line in textarray]
print(textarray)

# Make 2D array 1s and 0s
#
binary_array = [[("1" if cell == "@" else "0") for cell in row] for row in textarray]
binary_array = np.array(binary_array).astype("int")

# Add zeros border around
shape = binary_array.shape

binary_array = np.insert(
    binary_array, 0, np.zeros(shape[0], dtype=int), axis=0
)  # add 0s as first row
binary_array = np.insert(
    binary_array, shape[0] + 1, np.zeros(shape[0], dtype=int), axis=0
)  # add 0s as last row
binary_array = np.insert(
    binary_array, 0, np.transpose(np.zeros(shape[1] + 2, dtype=int)), axis=1
)  # add 0s as first row
binary_array = np.insert(
    binary_array, shape[1] + 1, np.transpose(np.zeros(shape[1] + 2, dtype=int)), axis=1
)  # add 0s as first row

print(binary_array)
shape = binary_array.shape


# Create function to count the 8 squares around
def countaround(nparray, x, y):
    sumneighbour = 0
    for i in range(x - 1, x + 2):
        # print(f"i is {i}")
        for j in range(y - 1, y + 2):
            # print(f"j is {j}")
            sumneighbour += nparray[i][j]
    return sumneighbour


# Create function to traverse array
totalsum = 0
for i in range(1, shape[0] - 1):
    for j in range(1, shape[1] - 1):
        print(f"row {i}, column {j} is {binary_array[i][j]}")
        # sumneighbour = countaround(binary_array, i, j)
        if binary_array[i][j] == 1:
            sumneighbour = countaround(binary_array, i, j)
            print(f"sumneighbour is {sumneighbour}")
            if sumneighbour < 5:
                totalsum += 1

print(f"totalsum is {totalsum}")
