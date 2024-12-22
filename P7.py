'''
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13,
What is the 10001st prime number?
'''

def isPrime(num):
    prime = True
    for j in range(2,num):
        if num%j == 0:
            prime = False
            break
    return(prime)

def nthPrime(num):
    number = 2
    count = 1
    while count < num:
        number += 1
        if isPrime(number):
            count += 1
    return number

print(nthPrime(10001))

