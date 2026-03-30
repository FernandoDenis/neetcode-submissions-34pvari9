class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #         i
        # [2,4,-4,-1]
        
        # stack [2]
        stack = []

        for rock in asteroids:
            if rock < 0:
                if stack and stack[-1] > 0:
                    rockExplote = False
                    realRock = abs(rock)
                    while stack and stack[-1] > 0:
                        if stack[-1] > realRock:
                            rockExplote = True
                            break
                        elif stack[-1] < realRock:
                            stack.pop()
                        else:
                            rockExplote = True
                            stack.pop()
                            break
                    if not rockExplote:
                        stack.append(rock)
                    continue
                stack.append(rock)
            else:
                stack.append(rock)

        return stack