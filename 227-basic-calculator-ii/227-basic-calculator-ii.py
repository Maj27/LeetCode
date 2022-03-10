class Solution:
    def calculate(self, s: str) -> int:
        chars = [c for c in s if c!=' ']
        num = 0
        prev_opr = '+'
        stack = []
        
        for c in chars:
            if c.isdigit():
                num = num*10 + int(c)	 
            else:
                if prev_opr == '+':
                    stack.append(num)
                elif prev_opr == '-':
                    stack.append(-num)
                elif prev_opr == '*':
                    stack[-1] *= num
                elif prev_opr == '/':
                    stack[-1] = (int)(float(stack[-1])/float(num))

                num = 0
                prev_opr = c

        if prev_opr == '+':
            stack.append(num)
        elif prev_opr == '-':
            stack.append(-num)
        elif prev_opr == '*':
            stack[-1] *= num
        elif prev_opr == '/':
            stack[-1] = (int)(float(stack[-1])/float(num))
  
        return sum(stack)
