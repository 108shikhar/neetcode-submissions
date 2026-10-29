class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
            self.d[key].append([timestamp,value]) 
        elif key in self.d:
            self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        else:
            l,h=0,len(self.d[key])-1
            ans=""
            while l<=h:
                m=(l+h)//2
                if self.d[key][m][0]>timestamp:
                    h=m-1
                else:
                    l=m+1
                    ans=self.d[key][m][1]
            return ans
        
