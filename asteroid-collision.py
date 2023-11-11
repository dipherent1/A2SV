class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        approch:
        this is going to be something like a monotonic stack

        we will append 1 by 1 
        
        we will only pop is stack[-1] is positive and ast is negative 
        
        we dont need to compare their absolute values because we can just sum then and check if the sum is positive or negative

        if sum>0 we dont append
        if sum<0 we pop
        if sum == 0 we pop but we dont append
        edge case:
        cancel out

        we will only append if sum !>=0
        '''
        stack = []
        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
                sum = stack[-1]+ast
                if sum>0:
                    ast = 0
                elif sum <0:
                    stack.pop()
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        return stack