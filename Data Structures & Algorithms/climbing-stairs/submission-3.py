class Solution:
    def climbStairs(self, n: int) -> int: 
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)
    #  -1      -2
        #  38
    #   37   1
#     36   20  2
#   35

