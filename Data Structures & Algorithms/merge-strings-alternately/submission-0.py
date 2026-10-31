class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        a,b=0,0
        while a<len(word1) and b<len(word2):
            res=res+word1[a]
            res=res+word2[a]
            a,b=a+1,b+1
        while a<len(word1):
            res=res+word1[a]
            a=a+1
        while b<len(word2):
            res=res+word2[b]
            b=b+1
        return res
            