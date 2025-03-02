'''
The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
#This question is worded weirdly... Think you do the subtraction backwards

def sum_squares(n):
    total = 0
    for i in range(1,n+1):
        total += i**2
    return total

def square_sum(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return(total**2)

print(square_sum(100)-sum_squares(100))