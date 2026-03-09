class Solution:
    def combinationSum(self, candidates, target):
        result = []
        

        def backtrack(index, current_combination, current_sum):
          
            if current_sum == target:
                result.append(list(current_combination))
                return
            
       
            if current_sum > target or index >= len(candidates):
                return
            
           
            current_combination.append(candidates[index])
            backtrack(index, current_combination, current_sum + candidates[index])
            
          
            current_combination.pop()
    
            backtrack(index + 1, current_combination, current_sum)

        backtrack(0, [], 0)
        return result
