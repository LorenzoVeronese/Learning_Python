"""
---PART ONE---
"""
"""
PSEUDOCODE
set the list of spoken nums as the starting list
for i <= 2019 - len(starting list)
      if the previous number is in the list only one time
            say 0
      else
            calculate the difference between the last two occurrences 
                  of that number
            say the result
"""

starting = (0, 12, 6, 13, 20, 1, 17)

spoken = list(starting)
prev = spoken[-1]
for i in range (len(starting) - 1, 2019):
      occur = spoken.count(prev)
      #print(occur)
      if occur <= 1:
            spoken.append(0)
      else:
            turns = []
            #count backwards
            count = 0
            j = i
            while count != 2 and j >= 0:
                  if spoken[j] == prev:
                        count += 1
                        turns.append(j)
                  j -= 1
            spoken.append(turns[0] - turns[1])
            
      prev = spoken[i + 1]
      
print(spoken[-1])