'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers
'''

def isPalindrome(number):
    for i in range(0,int(len(number)/2)):
        if number[i] != number[int(len(number)-i-1)]:
            return(False)
    return(True)

record = 0

for i in range(1000):
    for j in range(1000):
        test = i*j
        if isPalindrome(list(map(int, str(test)))) == True and test > record:
            record = test

print(record)


