class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:
            if not stack or ast > 0 or stack[-1] < 0:
                stack.append(ast)

            while stack and ast < 0 and stack[-1] > 0:
                lastValue = stack.pop()

                if lastValue == abs(ast):
                    break
                elif lastValue + ast > 0:
                    stack.append(lastValue)
                    break
                elif stack and stack[-1] > 0:
                    continue
                else:
                    stack.append(ast)

        return stack




        