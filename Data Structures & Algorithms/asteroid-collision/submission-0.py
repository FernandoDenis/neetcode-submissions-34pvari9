class Solution:
    #      a
    # [-2,-2,1,-2]
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        completes_asteroids = [] # [-2,-2,1]
        for ast in asteroids:
            if not completes_asteroids:
                completes_asteroids.append(ast)
                continue
            
            last_asteroid = completes_asteroids[-1] # -2

            if (last_asteroid < 0 and ast < 0 ) or (last_asteroid > 0 and ast > 0) or (last_asteroid < 0 and ast > 0):
                completes_asteroids.append(ast)
                continue

            while last_asteroid > 0 and ast < 0:
                if last_asteroid > abs(ast):
                    break
                elif last_asteroid < abs(ast):
                    completes_asteroids.pop()
                    if completes_asteroids:
                        last_asteroid = completes_asteroids[-1]
                    else:
                        completes_asteroids.append(ast)
                        break
                else:
                    if completes_asteroids:
                        completes_asteroids.pop()
                        break
                    else:
                        completes_asteroids.append(ast)
                        break
                        
            if (last_asteroid < 0 and ast < 0 ) or (last_asteroid > 0 and ast > 0) or (last_asteroid < 0 and ast > 0):
                completes_asteroids.append(ast)
                continue


        return completes_asteroids