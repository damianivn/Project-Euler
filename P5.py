'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number that 
is evenly divisible by all of the numbers from 1 to 20
'''
import time

def factorize(n):
    num=int(n)

    factors = []
    factored = False
    
    while factored == False:
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

for i in range(4,6):
    listFactors = factorize(i)

    for j in range(0,len(listFactors)):
        print(listFactors[j])


#print(factorize(16))
'''
testDict = {
    1:2,
    2:1,
    3:3
}
testDict.update({4:4})
print(testDict)
total = 1
for i in testDict:
    total*=i**(testDict.get(i))
'''
#print(total)


# answer = 1*2*3*2*5*7*2*3*11*13*2*17*19