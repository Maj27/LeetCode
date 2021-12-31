class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack or ast>0:
                stack.append(ast)
            elif ast<0:
                while stack and  stack[-1]>0 and abs(ast)>stack[-1]:
                    stack.pop()

                if not stack or stack[-1]<0:
                    stack.append(ast)
                elif abs(ast)==stack[-1]:
                    stack.pop()

        return stack	
    
        