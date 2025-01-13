import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = math.factorial(n)
        count = 0
        
        while result % 10 == 0:
            count += 1
            result //= 10

        return count