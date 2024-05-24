class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #Time Complexity: O(n)
        #Stack 
        
        stack = [] #[char, count]
        
        for c in s:
            #if the current char is equal to the char at the top of the 
            #stack then we are going to increment the count of the char in stack 
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1 
            else:
                #if the stack is empty or if we see a different char than 
                #the top of the stack then we are going to append the 
                #new char and its count to the stack 
                stack.append([c,1])
                
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        for char, count in stack:
            res += (char * count)
        return res 