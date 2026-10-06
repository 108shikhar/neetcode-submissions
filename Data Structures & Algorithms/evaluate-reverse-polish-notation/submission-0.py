class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for x in tokens:
            if x not in ('+', '-', '*', '/'):
                stk.append(int(x))
            else:
                b = stk.pop()
                a = stk.pop()

                if x == '+':
                    stk.append(a + b)
                elif x == '-':
                    stk.append(a - b)
                elif x == '*':
                    stk.append(a * b)
                elif x == '/':
                    stk.append(int(a / b))

        return stk[-1]