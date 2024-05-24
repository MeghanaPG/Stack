class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #Time and Memory complexity: O(n) (bcz we are using extra memory->stack)
        #Stack 
        #for example the number should be of type 142: 1 < 2 < 4 
        stack = [] #pair [num, minLeft], monotonically decreasing
        curMin = nums[0]
        
        #We are skipping the first value because it can't be the 
        #j or k value anyways 
        for n in nums[1:]:
            #if there are any smaller values than it on the stack 
            #then we are going to pop it 
            while stack and n >= stack[-1][0]:
                stack.pop()
            #Basically it has to be lesseer than the top of the stack and 
            #greater than the minimum seen so far in the stack 
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True 
            
            stack.append([n,curMin])
            curMin = min(curMin, n)
        return False 
    