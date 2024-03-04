class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        myStack = []
        
        for c in tokens:
            if c == "*":
                myStack.append(int(myStack.pop()) * int(myStack.pop()))
            elif c == "+":
                myStack.append(int(myStack.pop()) + int(myStack.pop()))
            elif c == "-":
                m1 = int(myStack.pop()) 
                m2 = int(myStack.pop())
                myStack.append(int(m2) - int(m1))
            elif c == "/":
                 m1 = int(myStack.pop()) 
                 m2 = int(myStack.pop())
                 myStack.append(int(m2/m1))
            else:
                 myStack.append(c)
        return int(myStack[0])