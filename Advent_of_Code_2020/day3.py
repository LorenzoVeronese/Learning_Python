"""
---PART ONE---
"""
"""
PSEUDOCODE
for each line of the file
      read the last+3 position and check
NOTES
lenght of a line is len(line)-1=31. It goes from 0 to 30
"""

filename = "day3.txt"
with open(filename, 'r') as map_file:
      cursor = 0
      count = 0
      #I dont't consider the first line
      first = 1
      for line in map_file:
            if first:
                  first = 0
                  continue   
            #change actual position to consider
            cursor += 3
            if cursor > 30:
                  #find quantity of which I exceed from the map
                  adding = cursor - 30
                  cursor = adding - 1
            #check if it's a tree: if it is, increment count
            if line[cursor] == '#':
                  count += 1
print(count)

"""
---PART TWO---
The following function, works also on the first part
"""
#I's better to define a function not to repeat the code. This function
#works also for part one
def tree_counter_lines(filename, right, line_shift):
      with open(filename, 'r') as map_file:
            cursor = 0
            count = 0
            #I want multiples of line_shift
            line_counter = 0
            for line in map_file:
                  #I don't consider the first line
                  if line_counter == 0:
                        pass
                  elif line_counter % line_shift == 0:
                        #change actual position to consider
                        cursor += right
                        if cursor > 30:
                              #find quantity of which I exceed from the map
                              adding = cursor - 30
                              cursor = adding - 1
                        """
                        testing
                        print(cursor)
                        print(line[cursor])
                        """
                        #check if it's a tree: if it is, increment count         
                        if line[cursor] == '#':
                              count += 1
                  line_counter += 1
      return count

result = 1
result = result * tree_counter_lines(filename, 1, 1)
result = result * tree_counter_lines(filename, 3, 1)
result = result * tree_counter_lines(filename, 5, 1)
result = result * tree_counter_lines(filename, 7, 1)
result = result * tree_counter_lines(filename, 1, 2)
print(result)
