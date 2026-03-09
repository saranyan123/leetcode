class Solution:
    def trap(self, height): 

        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
          
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water

# --- Testing the code ---
sol = Solution()
example1 = [0,1,0,2,1,0,1,3,2,1,2,1]
example2 = [4,2,0,3,2,5]

print("Result for Example 1:", sol.trap(example1)) 
print("Result for Example 2:", sol.trap(example2)) 
