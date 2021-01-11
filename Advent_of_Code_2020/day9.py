"""
---PART ONE---
"""
"""
PSEUDOCODE
put each number of the file into a tuple
consider a list of the previous 25 numbers and see if it's the sum of
      two of them
"""

def make_xmas_tuple(filename):
      """
      PARAMETHER
      filename: string, name of the file to read
      RETURN
      tuple, containing all numbers in the file
      """
      with open(filename, 'r') as xmas_file:
            xmas_list = []
            for line in xmas_file:
                  if line[len(line) - 1] == '\n':
                        line = line[0 : len(line) - 1]
                  xmas_list.append(int(line))
      return tuple(xmas_list)

def who_not_sum(xmas_tuple, previous):
      """
      PARAMETHER
      xmas_tuple: tuple, containing all numbers
      previous: int, how many previous numbers can form the couple to
            be summed
      RETURN
      int, number which isn't the sum of the previous ones

      EXECUTION
      for every number I consider:  from actual_index - previous
            to previous - 1 and look among them for the couple to sum
            if I can't find the tuple
                  return actual number     
      """
      #this find the number to obtain as sum
      #start from index = previous
      for i in range(previous, len(xmas_tuple)):
            #first number to sum
            for j in range(i - previous, i - 1):
                  #second number to sum
                  for k in range(i - previous + 1, i):
                        if xmas_tuple[j] + xmas_tuple[k] == xmas_tuple[i]:
                              break
                  if xmas_tuple[j] + xmas_tuple[k] == xmas_tuple[i]:
                        break
            if xmas_tuple[j] + xmas_tuple[k] != xmas_tuple[i]:
                  return xmas_tuple[i]
      return None
                  
filename = "day9.txt"
previous = 25
xmas_tuple = make_xmas_tuple(filename)
intruder = who_not_sum(xmas_tuple, previous)
print(intruder)


"""
---PART TWO---
"""

def find_couple(xmas_tuple, minimum = 2):
      lenght = minimum
      while 1:
            for x in range(len(xmas_tuple) - lenght):
                  res = sum(xmas_tuple[x : x + lenght])
                  if res == intruder:
                        return min(xmas_tuple[x: x + lenght]), \
                              max(xmas_tuple[x: x + lenght])
            lenght += 1

print(sum(find_couple(xmas_tuple)))  
