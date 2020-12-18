"""
---PART ONE---
"""
"""
PSEUDOCODE
create a list of lists of lists which has at the center the puzzle input; 
      around it there're 6 more lines/column for each side. These ones are void('.')
apply conditions

NOTES
structure of the space:
      y[
            x[
                  z[
                        
                  ]
            ]
      ]
"""
import copy

def mk_space(filename):
      #count how long are edges af the cube
      with open(filename, 'r') as fd:
            lenght = len(fd.readline()) - 1

      #create a completely matrix bigger than the one given, with all '.'
      #list contains ys
      #y indexes lines
      #which contain xs
      #x indexes depth
      #which contains zs
      space = []
      for y in range(0, lenght + 12):
            #append a line
            space.append([])
            for x in range(0, lenght + 12):
                  #each element of the line (x) has a depth associated
                  space[y].append([])
                  for z in range(0, 13):
                        #elements in the depth
                        space[y][x].append('.')
      
      with open(filename, 'r') as fd:
            #the first line of the space to fill is line 6
            y = 6
            #central z coordinate
            z = 6
            for line in fd:
                  if line[-1] == '\n':      
                        line = line[0 : -1]
                  i = 0
                  for x in range(6, 6 + lenght):
                        space[y][x][z] = line[i]
                        i += 1
                  y += 1
      return space

def stay_active(space, y, x, z):
      count = 0
      for y_ in range(y - 1, y + 2):
            #to avoid index out of range error
            if y_ < 0 or y_ > (len(space) - 1):
                  continue
            for x_ in range(x - 1, x + 2):
                  if x_ < 0 or x_ > (len(space[y_]) - 1):
                        continue
                  for z_ in range (z - 1, z + 2):
                        if z_ < 0 or z_ > (len(space[y_][x_]) - 1):
                              continue
                        if y_ == y and x_ == x and z_ == z:
                              continue 
                        if space[y_][x_][z_] == '#':
                              count += 1
                        if count > 3:
                              return False
      if count == 2 or count == 3: 
            return True
      else:
            return False

def switch_to_active(space, y, x, z):
      count = 0
      for y_ in range(y - 1, y + 2):
            #to avoid index out of range error
            if y_ < 0 or y_ > (len(space) - 1):
                  continue
            for x_ in range(x - 1, x + 2):
                  if x_ < 0 or x_ > (len(space[y_]) - 1):
                        continue
                  for z_ in range(z - 1, z + 2):
                        if z_ < 0 or z_ > (len(space[y_][x_]) - 1):
                              continue
                        if y_ == y and x_ == x and z_ == z:
                              continue
                        if space[y_][x_][z_] == '#':
                              count += 1
                        if count > 3:
                              return False
      if count == 3:
            return True
      else: 
            return False

def simulation(space):
      #I need prev_space to avoid considering actual cycle
      #changes in changes to make (in other words: all changes are made 
      #looking at the previous cycle, not the one I'm modifying in the 
      #current cycle)
      prev_space = copy.deepcopy(initial_space)
      #for each element check if it switch to active/inactive
      for cycle in range(0, 6):
            prev_space = copy.deepcopy(space)
            '''
            to visualize slices of the space
            print()
            print("CYCLE: ", cycle)        
            for z in range(0, 13):
                  for y in range(0, len(space)):
                        for x in range(0, len(space[y])):
                              print(space[y][x][z], end='')
                        print()
                  print()
            '''

            for y, line in enumerate(initial_space):
                  for x, column in enumerate(initial_space[y]):
                        for z, depth in enumerate(initial_space[y][x]):
                              if space[y][x][z] == '#'  and not stay_active(prev_space, y, x, z):
                                    space[y][x][z] = '.'
                              elif space[y][x][z] == '.' and switch_to_active(prev_space, y, x, z):
                                    space[y][x][z] = '#'
            #print(space)

      count = 0
      for y in range(0, len(space)):
            for x in range(0, len(space[y])):
                  for z in range(0, len(space[y][x])):
                        if space[y][x][z] == '#':
                              count += 1

      return count

filename = 'day17.txt'
initial_space = mk_space(filename)
print(simulation(copy.deepcopy(initial_space)))