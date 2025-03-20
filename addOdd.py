sum = 0
for i in range(1000, 2001) :
    if i % 2 == 1 :
        sum+=i

print('sum = ', sum)

sum2 = 0
for i in range(1001, 2001, 2) :
    sum2 += i

print('sum2 = ', sum2)
