class Solution:
    def searchRange(self, nums, target):
        def findBound(isFirst):
            low = 0
            high = len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                 
                        high = mid - 1
                    else:
       
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound


        start = findBound(True)
        end = findBound(False)
        
        return [start, end]
