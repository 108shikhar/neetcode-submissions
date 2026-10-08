class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d,stk=[],[]
        for i in range(0,len(position),1):
            d.append([position[i], float((target-position[i])/speed[i])])
        d.sort(reverse=True)
        for i in range(0,len(d),1):
            if not stk or d[i][1]>stk[-1]:
                stk.append(d[i][1])
        return len(stk)