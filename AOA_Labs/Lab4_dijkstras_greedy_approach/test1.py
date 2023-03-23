rows, cols = (5, 5)
# method 2 1st approach
arr = [[0] * cols] * rows
# lets change the first element of the
# first row to 1 and print the array
arr[0][0] = 1

for row in arr:
    print(row)
print("====================")

arr = [[0 for i in range(cols)] for j in range(rows)]

# again in this new array lets change
# the first element of the first row
# to 1 and print the array
arr[0][0] = 1
for row in arr:
    print(row)
