class Solution:
    def climbStairs(self, n: int) -> int:
        #   3
        # 2   1
    #   1  0 0 -1
    #  0 -1
        def recursiveStairs(top, cache):
            if top == 0:
                return 1
            elif top < 0:
                return 0

            if top in cache:
                return cache[top]

            cache[top] = recursiveStairs(top - 1, cache) + recursiveStairs(top - 2, cache)

            return cache[top]

        return recursiveStairs(n, {})