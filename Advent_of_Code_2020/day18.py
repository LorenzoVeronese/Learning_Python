"""
---PART ONE---
"""
def between_parentheses(expression):
      bracket = 1
      expression = expression[1 : len(expression)]
      for i, ch in enumerate(expression):
            if ch == '(':
                  bracket += 1
            elif ch == ')':
                  bracket -= 1
            if bracket == 0:
                  return i

def calculate(expression):
      res = expression[0]
      if len(expression) == 1:
            res = int(res)
            return res 
      elif res.isdigit():
            res = int(res)
            if expression[1] == '+':
                  res += calculate(expression[2 : len(expression)])
            elif expression[1] == '*':
                  res *= calculate(expression[2 : len(expression)])
      elif res == '(':
            '''two cases:
                  1)single or nested parentheses couples
                  2)(...)...(...)
            '''
            close_bracket = between_parentheses(expression)
            res = calculate(expression[1 : close_bracket + 1])
            if len(expression) > close_bracket + 2:
                  if expression[close_bracket + 2] == '+':
                      res += calculate(expression[close_bracket + 3: len(expression)])
                  elif expression[close_bracket + 2] == '*':
                      res *= calculate(expression[close_bracket + 3: len(expression)])
      return res

def false_math(filename):
      with open(filename, 'r') as fd:
            res = 0
            for line in fd:
                  if line[-1] == '\n':
                        line = line[0 : -1]
                  #remove all spaces
                  line = line.replace(' ', '')
                  
                  #since I noticed I've written the recursive function calculate in
                  #such a way that I make operation from right to left instead of from
                  #left to right, I decided to simply invert the line before passing
                  #it to the function
                  line = line[::-1]
                  line_list = []
                  for ch in line:
                        line_list.append(ch)
                  for i, ch in enumerate(line_list):
                        if ch == ')':
                              line_list[i] = '('
                        elif ch == '(':
                              line_list[i] = ')'
                  inverted_line = ''
                  for ch in line_list:
                        inverted_line += ch
                  res += calculate(inverted_line)
      print(res)

filename = "day18.txt"
false_math(filename)