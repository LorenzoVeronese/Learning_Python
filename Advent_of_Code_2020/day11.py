"""
---PART ONE---
"""
"""
PSEUDOCODE
create a tuple representing the file
loop
      create two help lists:
            the first one is modified in the for
            the second one is used to check if there are no changes
      for each seat
            conditions of the text to empty or occupy the seat
"""
import copy

#mk means make
def mk_seats_tuple(filename):
      with open(filename, 'r') as seats_file:
            seats_list = []
            for line in seats_file:
                  if line[len(line) - 1] == '\n':
                        line = line[0 : len(line) - 1]
                  #convert each line into a list of characters
                  seats_list.append(tuple(line))
      return tuple(seats_list)    

def all_empty(seats_list, i, j):
      #ci = close seat i (row)
      #cj = close seat j (column)
      for ci in range(i - 1, i + 2):
            #if there's nothig at above of below
            if ci < 0 or ci > (len(seats_list) - 1):
                  continue
            for cj in range(j - 1, j + 2):
                  #if there's nothig at left of right
                  if cj < 0 or cj > (len(seats_list[ci]) - 1):
                        continue
                  #I don't consider the seat I want to occupy
                  elif ci == i and cj == j:
                        continue
                  if seats_list[ci][cj] == '#':
                        return False
            if cj < 0 or cj > (len(seats_list[ci]) - 1):
                        continue
      return True

def four_occupied(seats_list, i, j):
      #ci = close seat i (row)
      #cj = close seat j (column)
      count = 0
      for ci in range(i - 1, i + 2):
            #if there's nothig at above of below
            if ci < 0 or ci > (len(seats_list) - 1):
                  continue
            for cj in range(j - 1, j + 2):
                  #if there's nothig at left of right
                  if cj < 0 or cj > (len(seats_list[ci]) - 1):
                        continue
                  #I don't consider the seat I want to occupy
                  elif ci == i and cj == j:
                        continue
                  if seats_list[ci][cj] == '#':
                        count += 1
                        if count >= 4:
                              return True
            if cj < 0 or cj > (len(seats_list[ci]) - 1):
                        continue
      return False

def mk_distribution(seats_tuple):
      """
      PARATMETHER
      seats_tuple: tuple of tuples, containing each seat's condition
      RETURN
      list of lists, containing the stabilized map
      """

      #map of seats to modify
      curr = list(seats_tuple)
      for i in range(0, len(curr)):
            curr[i] = list(curr[i])
      #previous: to take track of the last distribution at each loop
      #This, not only to check if the previous list is the same as the
      #current one, but also because each seat is changed not considering
      #the changes which have just occurred in the loop
      #NB: list(curr)! Otherways, they map the same list
      prev = copy.deepcopy(curr)
      while 1:
            for i, row in enumerate(prev):
                  for j, col in enumerate(prev[i]):
                        if prev[i][j] == 'L' and all_empty(prev, i, j):
                              curr[i][j] = '#'
                        elif prev[i][j] == '#' and four_occupied(prev, i, j):
                                    curr[i][j] = 'L'
            '''debug
            print('curr-------------')
            for row in curr:
                  print(row)
            print('prev-------------')
            for row in prev:
                  print(row)'''
            if curr == prev:
                  return curr
            #print('next loop**************')
            prev = copy.deepcopy(curr)

filename = "day11.txt"
seats_tuple = mk_seats_tuple(filename)
'''debug
for row in seats_tuple:
      print(row)'''
distribution = mk_distribution(seats_tuple)
#print(distribution)
count = 0
for line in distribution:
      count += line.count('#')
print(count)