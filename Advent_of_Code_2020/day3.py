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
                  adding = (cursor) - 30
                  cursor = 0
                  cursor += adding - 1
            #check if it's a tree: if it is, increment count
            if line[cursor] == '#':
                  count += 1

print(count)