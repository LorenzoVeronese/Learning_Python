"""
---PART ONE---
I don't know why, but when I print the final list containing all bags
containing the shiny gold one, I get some '[...]' which are not printable
singularly (nor can they be eliminated) but still are counted in len(list). 
Anyway, if you count all these '[...]'s (by hand, physically counting 
them in the output) you obtain 93. If you subtract it to the list's lenght, 
you obtain the correct solution to the puzzle. 
I struggled for hours to understand why these '[...]' where put into the
list, but I couldn't come up to any conlusion: if you have and idea, please
contact me. 
"""
"""
PSEUDOCODE
create a dictionary {bigger bag :(contains) smaller bags}:
      for every line of the file
            drop the last \n character (the final line doesn't have it)
            1)take it's first two words: they are the color of the bigger bag
            2)for the entire string: go after a number, then take two words
            create a list[1) : 2)]
for every key of the dictionary
      if it contains shiny gold bag and it's not in the list, ad it to the list
list's len is the solution


NOTES:
structure of the file: color- bags contain &number -color-bags, number -color- bags.
      so each color is at the start or between bags and number
color is made up of two words separater by ' '
"""

def make_bags_dict(filename):
      """
      PARAMETHER
      filename: string, containing the name of the file
      RETURN
      list, mapping each bigger bag (listof two words) to the smaller ones (list of two words)
      """
      with open(filename, 'r') as bags_file:
            bag_map = {}
            #c_line means current line
            for c_line in bags_file:
                  if c_line[len(c_line) - 1] == '\n':
                        c_line = c_line[0 : len(c_line) - 1]

                  #need to find the index with the second space
                  #(before of it, there're the two bigger bag's color)
                  spaces = 0
                  for index, i in enumerate(c_line, 0):
                        if i == ' ':
                              spaces += 1
                        if spaces == 2:
                              big_bag = c_line[0 : index]
                              break
                  #this list contains the two colors
                  big_bag = big_bag.split(' ')

                  #dropping the first part of the line which I
                  #don't need anymore
                  c_line = c_line[index + 1 : len(c_line)]

                  #index signaling the start of two colors
                  index_start = 0
                  spaces = None
                  small_bag = []
                  for index, i in enumerate(c_line, 1):                      
                        #when I find a number, expect a smaller
                        #bag's color (two words)
                        if i.isnumeric():
                              index_start = index + 1
                              spaces = 0
                        #after the number I expect 3 spaces    
                        if i == ' ' and spaces != None:
                              spaces += 1
                              if spaces == 3:
                                    small_bag_single = c_line[index_start : index - 1]
                                    small_bag_single = small_bag_single.split(' ')                            
                                    small_bag.append(small_bag_single)
                                    small_bag = small_bag
                                    spaces = None
                        #I've finished the line, so I need to converge small_bag to big_bag
                        if i == '.':
                              bag_map[tuple(big_bag)] = small_bag
      return bag_map

def how_many_bags(bag_map, searched, found = []):
      """
      PARAMETHERS
      bag_mapping: dictionary, obtained from function above
      searched: a list, containing the two attributes of the bag I'm counting
      RETURN
      int, number of bags which can contain the searched
      """
      count = 0
      bag_map_temp = dict(bag_map)
      for bag in bag_map:
            if list(searched) in list(bag_map[bag]) and list(bag) not in found:
                  del bag_map_temp[bag]
                  found.append(how_many_bags(bag_map_temp, list(bag), found))
                  count += 1
      if count == 0:
            return list(searched)
      else:
            found.append(searched)
            return found

filename = "day7.txt"
bag_map = make_bags_dict(filename)
sol = []
sol = how_many_bags(bag_map, ['shiny', 'gold'])
print(sol)
print(len(sol))
