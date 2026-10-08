class Solution:
    def simplifyPath(self, path: str) -> str:
        res,stk="",[]
        for i in range(len(path)+1):
            c = path[i] if i<len(path) else "/"
            if c=='/':
                if res=="..":
                    if stk:
                        stk.pop()
                elif res!="" and res!=".":
                    stk.append(res)
                res=""
            else:
                res=res+c
        return "/"+"/".join(stk)