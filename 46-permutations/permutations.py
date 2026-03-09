class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, used):
      
            if len(path) == len(nums):
                result.append(path[:]) 
                return
            
            for i in range(len(nums)):
      
                if used[i]:
                    continue
                
          
                used[i] = True
                path.append(nums[i])
                
    
                backtrack(path, used)
                
           
                path.pop()
                used[i] = False
        
  
        backtrack([], [False] * len(nums))
        return result

sol = Solution()
print("Permutations of [1,2,3]:", sol.permute([1, 2, 3]))
print("Permutations of [0,1]:", sol.permute([0, 1]))
