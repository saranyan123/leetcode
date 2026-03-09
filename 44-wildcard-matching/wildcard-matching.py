class Solution:
    def isMatch(self, s, p):
        s_ptr = 0
        p_ptr = 0
        match_idx = 0
        star_idx = -1
        
        while s_ptr < len(s):
    
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
 
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1
            
         
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match_idx += 1
                s_ptr = match_idx
                
     
            else:
                return False
        
      
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)


sol = Solution()
print(sol.isMatch("aa", "a"))     
print(sol.isMatch("aa", "*"))     
print(sol.isMatch("cb", "?a"))    
print(sol.isMatch("adceb", "*a*b")) 
