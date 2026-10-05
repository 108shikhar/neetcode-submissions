class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        i=0
        while (i<len(operations)):
            x=operations[i]
            if x in ('+'):
                if stk:
                    one=stk[-1]
                    two=stk[-2]
                stk.append(one+two)
            elif x in ('C'):
                if stk:
                    stk.pop()
            elif x in ('D'):
                if stk:
                    last=stk[-1]
                    stk.append(2*last)
            elif (-30000<=int(x)<=30000):
                stk.append(int(x))
            i=i+1
        ans=0
        for i in stk:
            ans=ans+i
        return ans