class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Time Complexity: O(n)
        # stores the last occurence of c 
        last = {c:i for i,c in enumerate(s)}
        stack = []

        for i, c in enumerate(s):
            if c in stack:
                continue 
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)
