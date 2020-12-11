"""
---PART ONE---
"""
"""
PSEUDOCODE
put each number of the file into a tuple sorting them in increasing order
for each number of the tuple,
      if you can, choose the +1 adapter
      else choose the +3 one
      in the meanwhile, memorize the numbers of +1 and +3
"""

def make_tuple(filename):
      with open(filename, 'r') as adapt_file:
            adapt_list = []
            for line in adapt_file:
                  #drop \n at the end of the line
                  if line[len(line) - 1] == '\n':
                        line = line[0 : len(line) - 1]
                  adapt_list.append(int(line))
            
            adapt_list.sort()
            #append the +3 from the last adapter to the phone
            adapt_list.append(adapt_list[len(adapt_list) - 1] + 3)
      return tuple(adapt_list)

def find_product(adapt_tuple):
      num1 = 0
      num3 = 0
      prev = adapt_tuple[0]
      if prev == 1:
            num1 += 1
      elif prev == 3:
            num3 += 1
      for el in adapt_tuple:
            #if it's the first loop, go over
            if el == prev:
                  continue
            if el - prev == 1:
                  num1 += 1
            elif el - prev == 3:
                  num3 += 1
            #if the difference is 2, it means that I had to take the
            #previous number as +3, not +1
            elif el - prev == 2:
                  num1 -= 1
                  num3 += 1
            prev = el        
      return num1 * (num3)

filename = "day10.txt"
adapt_tuple = make_tuple(filename)
print(find_product(adapt_tuple))