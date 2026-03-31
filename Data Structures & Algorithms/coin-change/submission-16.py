class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        q = deque()
        q.append(0)

        seen = set()
        numCoins = 0

        while q:

            for _ in range(len(q)):
                val = q.popleft()

                for coin in coins:

                    if coin + val == amount:
                        return numCoins + 1
                    elif coin + val < amount and coin + val not in seen:
                        q.append(coin + val)
                        seen.add(coin + val)

            numCoins += 1

        return -1
