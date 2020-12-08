"""
---PART ONE---
"""
"""
PSEUDOCODE
global acc
put each line of the file in a list of lists, where every list is [string, int]; then
      convert it to a tuple (I don't want to touch it in the future: it's my "database")
Re-obtain a list version of the tuple just created and append at each inner list its index
delete from the list all instructions (with their index) executed
      when you can't find the current instruction in the list, return acc
      otherways execute instruction
"""
#global variable
acc = 0

def make_instr_tuple(filename):
      with open(filename) as instr_file:
            instr_tuple = []
            for line in instr_file:
                  #drop the terminator character \n
                  if line[len(line) - 1] == '\n':
                        line = line[0 : len(line) - 1]
                  
                  #split the line
                  #take it's instruction
                  instr = line[0 : 3]
                  #take it's value
                  value = int(line[4 : len(line)])
                  #put them into the list as a tuple
                  instr_tuple.append((instr, value))

      return tuple(instr_tuple)

def find_loop(instr_tuple):
      global acc
      #create the list version of the tuple with an index at
      #the end (go below for the explaining)
      instr_list = list(instr_tuple)
      for i, el in enumerate(instr_list):
            #transform the tuple into list
            instr_list[i] = list(instr_list[i])
            #append instruction's index
            instr_list[i].append(i)

      i = 0
      while 1:
            #take the instruction from the tuple and convert it
            #into a list
            instr = list(instr_tuple[i])
            #create a support variable in which to copy the current
            #instructin; then I append the current index
            instr_check = list(instr)
            instr_check.append(i)
            #if i can't find the instr_check, it means that
            #I've just executed it (this is why I appended the
            #index of each instruction: each of them can be repeated
            #multiple times in the file, so I need to distinguish
            #the single instruction among its copies)
            if instr_check not in instr_list:
                  return acc
            #I it's the first time I execute the instructin, I
            #remove it from the list, so I'll not find it in
            #the future
            else:
                  instr_list.remove(instr_check)
            #execute acc
            if instr[0] == 'acc':
                  acc += instr[1]
                  i += 1
            #execute jump
            elif instr[0] == 'jmp':
                  i += instr[1]
            #execute nop
            else:
                  i += 1

filename = "day8.txt"
instr_tuple = make_instr_tuple(filename)
print(find_loop(instr_tuple))