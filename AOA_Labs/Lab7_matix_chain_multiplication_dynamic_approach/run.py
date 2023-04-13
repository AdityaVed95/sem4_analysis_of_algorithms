# assume number of matrices is 4
def print_parenthesis(s, i, j):
    if i == j:
        print("A{}".format(i), end='')
    else:
        print("(", end='')
        print_parenthesis(s, i, s[i][j])
        print_parenthesis(s, s[i][j] + 1, j)
        print(")", end='')


n = 5
p = [5, 4, 6, 2, 7]
print("Given dimensions of matrices are : ", p, end='\n\n')

m = [[0 for i in range(n)] for j in range(n)]
s = [[0 for i in range(n)] for j in range(n)]

for d in range(1, n - 1):  # for(d=1;d<n-1;d++)
    for i in range(1, n - d):
        j = i + d
        minimum = float('inf')
        for k in range(i, j):
            q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
            if q < minimum:
                minimum = q
                s[i][j] = k

        m[i][j] = minimum

print("The Cost table is : ")
for row in m:
    print(row)

print("")

print("The K table is : ")
for row in s:
    print(row)

print("")
print("Thus minimum no of multiplications needed to multiply these 4 matrices is : ", m[1][n - 1])

print("\nThe optimal parenthesis for the given matrices is : ", end='')
print_parenthesis(s, 1, n - 1)
print("")
