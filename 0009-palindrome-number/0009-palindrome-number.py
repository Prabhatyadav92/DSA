class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        if x<0:
            return False
        rem=0
        dig=0
        while(y>0):
            rem=y%10
            y=y//10
            dig=dig*10+rem
        return x==dig
        