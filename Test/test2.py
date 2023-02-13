n = 54 # for higher values of n ( n >= 54) : the value of the sum = 1
sum = 0

for i in range (1,n+1):
    sum = sum + 1/(2**i)

print(sum)