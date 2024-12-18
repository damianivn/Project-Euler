'''
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''

Sequence = [1,2]
i=3
while i < 4000000:
    Sequence.append(i)
    i=(Sequence[len(Sequence)-1] + Sequence[len(Sequence)-2])

sum = 0

for i in Sequence:
    if i%2 == 0:
        sum += i

print(sum)