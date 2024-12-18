'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 
'''

# Determine if a number is prime
def isPrime(num):
    prime = True
    for j in range(2,num):
        if num%j == 0:
            prime = False
            break
    return(prime)

max = 600851475143

for i in range(1,max):
    if max%i == 0:
        print(isPrime(int(max/i)))
        if isPrime(int(max/i)) == True:
            print(max/i)
            break