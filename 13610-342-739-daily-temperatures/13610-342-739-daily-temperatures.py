class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        tempStack = []

        for i, temp in enumerate(temperatures):
            while tempStack and temp > temperatures[tempStack[-1]]:
                prev_idx = tempStack.pop()
                res[prev_idx] = i - prev_idx 
            tempStack.append(i)
        return res 


    