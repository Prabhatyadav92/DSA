class Solution:
    def countCommas(self, n: int) -> int:
        total_commas=0
        th=1000
        while n>= th:
            total_commas +=(n-th)+1
            th *=1000
        return total_commas

       
        
        