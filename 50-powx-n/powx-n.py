class Solution:
    def myPow(self, x, n):
     
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x

        while n > 0:
           
            if n % 2 == 1:
                result = result * current_product
            
   
            current_product = current_product * current_product
            n = n // 2
            
        return result


sol = Solution()


print("Example 1 (2^10):", sol.myPow(2.0, 10))
print("Example 2 (2.1^3):", sol.myPow(2.1, 3))
print("Example 3 (2^-2):", sol.myPow(2.0, -2))
