from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
   
        anagram_map = defaultdict(list)
        
        for s in strs:
           
            sorted_key = "".join(sorted(s))
            
        
            anagram_map[sorted_key].append(s)
            
       
        return list(anagram_map.values())


sol = Solution()
print("Example 1:", sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
