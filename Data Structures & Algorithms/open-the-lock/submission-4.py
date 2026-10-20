class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 
        visit=set(deadends)
        q=deque()
        q.append(["0000",0])
        def locks(ans):
            res=[]
            for i in range(len(ans)):
                digit=str((int(ans[i])+1)%10)
                res.append(ans[:i]+digit+ans[i+1:])
                digit=str((int(ans[i])-1)%10)
                res.append(ans[:i]+digit+ans[i+1:])
            return res
        while q:
            val=q.popleft()
            lock,turn=val[0],val[1]
            visit.add(lock)
            if lock==target:
                return turn
            else:
                for child in locks(lock):
                    if child not in visit:
                        q.append([child,turn+1])
                        visit.add(child)
        return -1
