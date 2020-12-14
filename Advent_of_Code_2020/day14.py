"""
---PART ONE---
"""
"""
PSEUDOCODE
while line without 'mask'
      store bitmask
      store number converted into binary
      make comparison
      convert into decimal
      if the value is different from zero, store it into a list

NOTES
from decimal to binary (but I'll use the inbuilt functions)
      repeated divisions
      10 = 2^3 + 2^1 = 1010
      10 | 2  0
      5  | 2  1
      2  | 2  0
      1  | 2  1
      0  |
      
      I'll not use it
      def decimal_to_binary(decimal):
            binary = []
            while decimal != 0:
                  binary.insert(0, decimal % 2)
                  decimal = int(decimal / 2)

            #join elements of the list into a string and then into a number
            result = ''.join(str(digit) for digit in binary)

            return int(result)
"""

#learned new things on: https://stackoverflow.com/questions/6494915/regex-pattern-to-match-the-end-of-a-string
#     https: // stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python
#import regex module
import re

def apply_mask(bitmask_str, value):
      """
      PARAMETHERS
      bitmask: str, sequence of characters representing the bitmask
      value: int, decimal number which I add to the memory

      RETURN
      int, decimal value corresponding to the number to save in memory
      """
      #convert string into list
      bitmask = []
      bitmask[:0] = bitmask_str
      #convert value into binary and then into list
      value_str = str("{0:b}".format(value))
      value = []
      value[:0] = value_str

      #add 0s at the start of value until it's as long as bitmask
      missing = len(bitmask) - len(value)
      while missing != 0:
            value.insert(0, '0')
            missing -= 1
      #apply bitmask
      result_list = []
      for i, mask in enumerate(bitmask):
            if mask == 'X':
                  result_list.append(int(value[i]))
            else:
                  result_list.append(int(mask))

      #converting the list result into a string and then into a decimal number
      result = ''.join(str(digit) for digit in result_list)
      result = int(result, 2)

      return result

def mk_sum(filename):
      with open(filename, 'r') as fd:
            #memo is a dictionary memo_pos:value
            memo = {}
            for line in fd:                 
                  #if I've a new mask, change it
                  if line[0 : 4] == 'mask':
                        #using regular expressions to find the last number of the line
                        #( ) means group
                        #| means or
                        #[0-1] means a number 0 or 1
                        #[^( )] means until there're no more spaces
                        #* means all
                        #$ means end of the string
                        #so: 'take all characters after the last space of the string until the end'
                        #fd.readline()[0 : -1] means I take the line without the last character (\n)
                        #[0] at the end means I take the first corrispondence I found
                        bitmask = re.search(r'(X|[0-1])([^( )]*)$', line[0: -1])[0]                                       
                        continue
                  #this finds the two numbers of each line
                  numbers = re.findall(r'\d+', line)
                  #note that these are strings
                  memo_pos = int(numbers[0])
                  value = int(numbers[1])
                  memo[int(memo_pos)] = apply_mask(bitmask, value)

            result = 0
            for value in memo.values():
                  result += value

            return result

filename = "day14.txt"
print(mk_sum(filename))