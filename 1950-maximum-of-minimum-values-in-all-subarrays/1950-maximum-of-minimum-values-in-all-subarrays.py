class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        max_val_by_len = defaultdict(int)
        n = len(nums)
        nums.append(0)
        stack = [-1]

        for i in range(n+1):
            while nums[i] < nums[stack[-1]]:
                w = i - stack[-2] - 1
                max_val_by_len[w] = max(max_val_by_len[w], nums[stack.pop()])
            stack.append(i)
        res = [0] * n 
        for l in range(n, 0, -1):
            res[l-1] = max(res[l] if l<n else 0, max_val_by_len[l])
        return res 