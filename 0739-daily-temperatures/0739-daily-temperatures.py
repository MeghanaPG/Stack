class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [] 
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while tempStack and temp > temperatures[tempStack[-1]]:
                print(temperatures[tempStack[-1]])
                # keeping the track of prev idx 
                prev_idx = tempStack.pop()
                result[prev_idx] = idx - prev_idx 
            tempStack.append(idx)
        return result 















   
        