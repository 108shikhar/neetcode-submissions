class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        for c in s:
            if c!=']':
                stk.append(c)
            elif c==']':
                ans=""
                while stk and stk[-1]!='[':
                    ans=stk[-1]+ans
                    stk.pop()
                stk.pop()
                val=""
                while stk and stk[-1].isdigit():
                    val=stk[-1]+val
                    stk.pop()
                res=ans*int(val)
                stk.append(res)
                res=""
        return "".join(stk)