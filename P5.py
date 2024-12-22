'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number that 
is evenly divisible by all of the numbers from 1 to 20
'''

def factorize(n):
    num=int(n)
    factors = []
    factored = False
    
    while not factored:
        for i in range(2,num+1):            
            if i == num:
                factors.append(num)
                factored = True
                break

            if num%i == 0:
                factors.append(i)
                num = num//i
                break

    return(factors)

primeFactors = {}

for i in range(2,21):
    listFactors = factorize(i)

    while listFactors:
        target = min(listFactors)
        counter = 0
        while target in listFactors:
            for j in listFactors:
                if j == target:
                    counter += 1
                    listFactors.remove(target)
        if primeFactors.get(target) is None:
            primeFactors[target] = counter

        elif primeFactors.get(target) < counter:
            primeFactors.update({target: counter})

print(primeFactors)
total = 1
for k in primeFactors:
    total *= k ** primeFactors[k]

print(total)