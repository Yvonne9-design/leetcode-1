Reverse Interger
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            # Check for potential overflow before updating rev
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and digit > 7):
                return 0
            rev = rev * 10 + digit
            x //= 10
            
        return sign * rev


        