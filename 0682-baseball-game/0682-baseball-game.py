class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack data structure 
        stack = []

        for op in operations:
            if op.lstrip('-').isdigit() or (op[0] == '-' and op[1:].isdigit()):
                stack.append(int(op))
            elif op == "+" and len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                mySum = n1 + n2 
                stack.append(n2)
                stack.append(n1)
                stack.append(mySum)
            elif op == "D" and len(stack) > 0:
                num = stack.pop()
                doubled_num = 2 * num
                stack.append(num)
                stack.append(doubled_num)
            elif op == "C" and len(stack) > 0:
                stack.pop()

        return sum(stack)

                