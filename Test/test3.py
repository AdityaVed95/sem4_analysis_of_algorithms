n = 100000000 # for higher values of n  : the value of the sum = 0.231
sum = 0

for i in range (1,n+1):
    sum = sum + ((3/16)**i)

print(sum)