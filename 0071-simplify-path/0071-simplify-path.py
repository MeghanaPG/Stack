class Solution:
    def simplifyPath(self, path: str) -> str:
        # Time Complexity: O(n)
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)