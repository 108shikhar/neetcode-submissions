class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m,x,y=len(s),{},{}
        for i in range(m):
            a,b=s[i],t[i]
            x[a]=x.get(a,0)+1
            y[b]=y.get(b,0)+1
        if x==y:
            return True
        else:
            return False