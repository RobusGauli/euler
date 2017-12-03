'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# here is the rudimentalry solution to the problem
def solution_one():
    multiple_of_3_or_5_upto1000 = set(range(0, 1000, 3)).union(set(range(0, 1000, 5))) - {0}
    print(sum(multiple_of_3_or_5_upto1000))


def solution_two():
    print(sum([i for i in range(1, 1000) if i%3 == 0 or i%5 == 0]))

#but this can get too slow if the number is more than 100000

#here is the constatnt time solution
#we know sum of multiple of 3  upto 1000 are 
# --> 3 + 6 + 9 + .... + 999
# --> 3 (1 + 2 + 3 + ... + 333)

#--> 3 * ((333 * 334) // 2)
#we know multiple of 5 are 5 * (1, 2, 3,4 ,5 ...)
#that is  --> 5 * ((n (n+1)) / 2)

def costly_solution(a, b, upto):
    return sum(set(range(0, upto, a)).union(set(range(0, upto, b))))


def right_solution(a, b, upto):
    #constantn time
    def sumDivisibleByNumber(n):
        #not including n
        _r =  (upto-1) // n
        return n * ((_r * (_r + 1))//2)
    
    return sumDivisibleByNumber(a) + sumDivisibleByNumber(b) - sumDivisibleByNumber(a * b)

    
print(right_solution(3, 5, 100000000))
    