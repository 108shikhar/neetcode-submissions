class MinStack:

    def __init__(self):
        self.stk=[]
        self.small=[]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.small or val<=self.small[-1]:
            self.small.append(val)
        
    def pop(self) -> None:
        if self.stk[-1] == self.small[-1]:
            self.small.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.small[-1]
