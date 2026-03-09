class Solution:
    def jump(self, nums):
   
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
  
        for i in range(len(nums) - 1):
       
            farthest = max(farthest, i + nums[i])
            
           
            if i == current_end:
                jumps += 1
                current_end = farthest
                
             
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps


sol = Solution()
print("Example 1:", sol.jump([2, 3, 1, 1, 4])) # 
print("Example 2:", sol.jump([2, 3, 0, 1, 4])) # 
