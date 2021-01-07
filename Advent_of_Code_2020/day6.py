"""
---PART ONE---
"""
"""
PSEUDOCODE
for line in file
      if not void line and not last line
            drop the final line's \n
            add to list each new letter
      else
            sum += len(list)
            list = []
"""
filename = "day6.txt"
with open(filename, 'r') as ticks:
      total_yes = 0
      yes_list = []
      for c_line in ticks:
            if c_line != '\n':
                  #the last line doesn't have \n at the end
                  if c_line[len(c_line) - 1] == '\n':
                        line = c_line[0 : len(c_line) - 1]
                  else:
                        line = c_line
                  for i in line:
                        if i not in yes_list:
                              yes_list.append(i)
            else:
                  total_yes += len(yes_list)
                  yes_list = []
      #adding the last number
      total_yes += len(yes_list)

print(total_yes)

"""
---PART TWO---
"""

fd = open("day6.txt")
whole = fd.read().split('\n\n')
groups = []
for group in whole:
      groups.append(group.split('\n'))
count = 0
for group in groups:
      for letter in group[0]:
            if all(letter in single_group for single_group in group):
                  count += 1
print(count)
