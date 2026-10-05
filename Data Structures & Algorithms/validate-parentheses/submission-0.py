class Solution:
    def isValid(self, s: str) -> bool:
        m=len(s)
        def solve(x,y):
            i,stk=0,[]
            while (i<y):
                if x[i] in ('(','[','{'):
                    stk.append(x[i])
                else:
                    if not stk:
                        return False
                    elif match(stk[-1],x[i])==False:
                        return False
                    elif match(stk[-1],x[i])==True:
                        stk.pop()
                i=i+1
            if stk:
                return False
            elif not stk:
                return True
        def match(a,b):
            if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
                return True
            else:
                return False
        return solve(s,m)