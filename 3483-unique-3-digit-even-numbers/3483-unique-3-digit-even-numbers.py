from collections import Counter
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        av_count=Counter(digits)
        u_ev_count=0
        for num in range(100,1000,2):
            d1=num//100
            d2=(num//10)%10
            d3=num%10

            re_count=Counter([d1,d2,d3])
            if all(av_count[d] >=re_count[d] for d in re_count):
                u_ev_count +=1
        return u_ev_count
        