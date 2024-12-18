#Find the sum of all the multiples of 3 or 5 below 1000

three = 0
five = 0

for i in range(1000):
    if (i % 3) == 0:
        three += i
    
    elif (i % 5) == 0:
        five += i

print(three+five)