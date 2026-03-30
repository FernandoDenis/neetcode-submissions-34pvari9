class Solution:
    def climbStairs(self, n: int) -> int: 

        def recursive(top, cache):
            if top == 0:
                return 1
            elif top < 0:
                return 0

            if top in cache:
                return cache[top]

            cache[top] = recursive(top - 1, cache) + recursive(top - 2, cache)

            return cache[top]

        return recursive(n, {})
    #  -1      -2
        #  38
    #   37   1
#     36   20  2
#   35

