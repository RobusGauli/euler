#largest prime factor of the number

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 
'''

#get the prime numbers upto 6008123
def is_prime(n):
    for i in range(2, (n//2 + 1)):
        if n% i == 0:
            #that means it is a prime
            return False
    return True


print(set(filter(is_prime, range(2, 600851475143))))
