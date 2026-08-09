s="nitin"
def is_paloindrome(s,left,right):
        if left>=right:
            return True
        if s[left]!=s[right]:
            return False
        return is_paloindrome(s,left+1,right-1)

print(is_paloindrome(s, 0, len(s)-1))
