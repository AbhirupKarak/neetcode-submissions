class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currSt = []
        ops = ["+", "-", "*", "/"]
        res = 0
        if len(tokens) == 1:
            return int(tokens[0])
        if not tokens:
            return 0
        for char in tokens:
            print(currSt)
            if char not in ops:
                currSt.append(char)
            else:
                op2 = int(currSt[-1])
                currSt.pop()
                op1 = int(currSt[-1])
                currSt.pop()
                if char == "+":
                    res = int(op1 + op2)
                elif char == "-":
                    res = int(op1 - op2)
                elif char == "*":
                    res = int(op1 * op2)
                elif char == "/":
                    res = int(op1 / op2)
                currSt.append(str(res))
        return int(res)

            
        