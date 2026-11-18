# https://leetcode.com/problems/palindrome-number/

# First Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : 
            return False
        else : 
            reverse_x = int(str(x)[::-1])
            if x == reverse_x : 
                return True

        return False