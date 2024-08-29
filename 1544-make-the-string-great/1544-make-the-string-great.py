class Solution:
    def makeGood(self, s: str) -> str:
        # Time and Space: O(n)
        myStack = []

        for c in s:
            if myStack and c.swapcase() == myStack[-1]:
                myStack.pop()
            else:
                myStack.append(c)
            
        return "".join(myStack)