def count_primes_nums(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

print('From 1-10 there are:', count_primes_nums(10), 'prime numbers')
print('From 1-100 there are:', count_primes_nums(100), 'prime numbers')
print('From 1-1000 there are:', count_primes_nums(1000), 'prime numbers')
print('From 1-10,000 there are:', count_primes_nums(10000), 'prime numbers')
print('From 1-100,000 there are:', count_primes_nums(100000), 'prime numbers')