class StockSpanner:

    def __init__(self):
        self.i=0
        self.stk=[]
        self.money=[]

    def next(self, price: int) -> int:
        self.money.append(price)
        while self.stk and self.money[self.stk[-1]]<=price:
            self.stk.pop()
        if len(self.stk)==0:
            span=self.i+1
        else:
            span=self.i-self.stk[-1]
        self.stk.append(self.i)
        self.i=self.i+1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)