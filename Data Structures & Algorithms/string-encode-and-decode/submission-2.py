class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i, j in enumerate(strs):
            x=strs[i]
            y=str(len(strs[i]))
            res=res+y
            res=res+"#"
            res=res+x
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j=j+1
            length=int(s[i:j])
            final=s[j+1:j+1+length]
            l.append(final)
            i=j+length+1
        return l
