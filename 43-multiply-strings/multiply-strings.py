class Solution:
    def multiply(self, num1, num2):
     
        if num1 == "0" or num2 == "0":
            return "0"
        
  
        res = [0] * (len(num1) + len(num2))
  
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
           
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
            
                mul = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                
      
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
                

        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:]))


sol = Solution()
print(sol.multiply("123", "456")) 
