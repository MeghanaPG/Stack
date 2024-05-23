class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Time Complexity: O(n)
        stack = []

        for a in asteroids:
            # this means collision is taking place 
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0 
                else:
                    a = 0 
                    stack.pop()
            if a:
                stack.append(a)
        return stack 