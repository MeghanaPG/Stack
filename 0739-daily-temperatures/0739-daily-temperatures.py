class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temperatures[temp_stack[-1]]:
                prev_idx = temp_stack.pop()
                res[prev_idx] = i - prev_idx
            temp_stack.append(i)
        return res
