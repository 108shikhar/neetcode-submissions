class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for i, j in enumerate(s):
            x=s[i]
            if x not in a:
                a[x]=1
            elif x in a:
                a[x]=a[x]+1
        for p, q in enumerate(t):
            y=t[p]
            if y not in b:
                b[y]=1
            elif y in b:
                b[y]=b[y]+1
        if a==b:
            return True
        elif a!=b:
            return False