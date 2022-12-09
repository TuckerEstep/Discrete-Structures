#Here is the formula I found online: p(n) = 1 - (364! / [365 - n]! )/365^(n-1)


import math


def birthday_probability_calc():
    print('How many people in the sample?')
    sample_size = int(input())
    birth_prob = 1 - (math.factorial(364) / math.factorial(365 - sample_size)) /365**(sample_size - 1)
    print('The chances of 2 people having the same birthday out of', sample_size, 'is:', (birth_prob * 100))
    
birthday_probability_calc()