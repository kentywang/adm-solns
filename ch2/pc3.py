from util import asserter

"""
Observations:
       123456789
start  000000000
i = 1 1|11111111
i = 2 10|1010101
i = 3 100|011100
i = 4 1001|11110
i = 5 10010|1110
i = 6 100100|110

- kinda like sieve of Eratosthenes
- means if nth bulb is prime, it always is off (toggled on in 1st walk, toggled off in nth walk )
- but if nth bulb isn't prime, answer is num_of_divisors % 2
- ex: 4's divisor is 1,2,4; so 3 divisors, odd number of divisors => on
- ex: 5's divisor is 1,5; so 2 divisors, even number => off
- ex: 6's divisor is 1,2,3,6; so 4 divisors, even number => off
"""


def num_of_divisors(n: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    ct = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ct += 1
    return ct


def is_bulb_on(n: int) -> bool:
    return num_of_divisors(n) % 2 == 1


asserter(lambda: is_bulb_on(1), True)
asserter(lambda: is_bulb_on(2), False)
asserter(lambda: is_bulb_on(3), False)
asserter(lambda: is_bulb_on(4), True)
asserter(lambda: is_bulb_on(5), False)
asserter(lambda: is_bulb_on(6), False)
asserter(lambda: is_bulb_on(6241), True)
asserter(lambda: is_bulb_on(8191), False)
