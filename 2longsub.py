class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l=0
        r=0
        n=len(s)
        my_dic={}
        while r<n:
            if s[r] in my_dic:
                l=max(l,my_dic[s[r]]+1)
            max_len=max(max_len,r-l+1)
            my_dic[s[r]]=r
            r +=1
        return max_len
        









        # max_len=0
        # for i in range(0,len(s)):
        #     my_set=set()
        #     for j in range(i,len(s)):
        #         if s[j] in my_set:
        #             break
        #         max_len=max(max_len,j-i+1)
        #         my_set.add(s[j])
        # return max_len
        
