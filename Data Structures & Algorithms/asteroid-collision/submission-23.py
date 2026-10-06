class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk,n=[],len(asteroids)
        for i in range(n):
            x=asteroids[i]
            if x>0:
                stk.append(x)
            elif x<0:
                while len(stk)!=0 and stk[-1]>0 and stk[-1]<abs(x):
                    stk.pop()
                if len(stk)!=0 and stk[-1]==abs(x):
                    stk.pop()
                elif len(stk)==0 or stk[-1]<0:
                    stk.append(x)
        return stk