class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        seen = set()

        # maintain a dictionary 
        last_occurrence = {c:i for i, c in enumerate(s)}
        

        for i, c in enumerate(s):
            if c not in seen:
                # if stack is not empty 
                # if the character we have is < top of stack 
                # if index i is not the last occurence 
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)