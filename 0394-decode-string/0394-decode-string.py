class Solution:
    def decodeString(self, s: str) -> str:
        # Time Compelxity: O(n)
        # Stack
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                # we will keep popping until we get the opening bracket 
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                # to make sure we are popping the "[" bracket
                stack.pop()
                # to take care of the digit 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                stack.append(int(k) * substr)
        return "".join(stack)
