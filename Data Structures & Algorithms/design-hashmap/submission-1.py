class MyHashMap:

    def __init__(self):
        self.a=[]
        self.b=[]

    def put(self, key: int, value: int) -> None:
        if key not in self.a:
            self.a.append(key)
            self.b.append(value)
        elif key in self.a:
            i=self.a.index(key)
            self.b[i]=value

    def get(self, key: int) -> int:
        if key in self.a:
            i=self.a.index(key)
            j=self.b[i]
            return j
        elif key not in self.a:
            return -1

    def remove(self, key: int) -> None:
        if key in self.a:
            i=self.a.index(key)
            del self.a[i]
            del self.b[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)