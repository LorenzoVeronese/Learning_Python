"""
---PART ONE/TW0---
"""
"""
PSEUDOCODE
for each line    
      put (x, x, letter) in a list, and password in a string
      check if the password fit constrains(function)
"""

def is_pass_valid(constrain, password):
      """
      TAKES
      constraint: a list, [int - min recurrences, 
                              int - max recurrences, 
                              string  - passwod]
      password: a string, the password to check
      RETURN
      True if the password is ok
      """
      count = 0
      for letter in password:
            if letter == constrain[2]:
                  count += 1
                  #check if there're too much recurrences
                  if count > constrain[1]:
                        return False
      #check if there're too few recurrences
      if count < constrain[0]:
            return False
      else:
            return True

def is_pass_valid2(constrain, password):
      print(constrain, password)
      return ((password[constrain[0] - 1] == constrain[2] \
            or password[constrain[1] - 1] == constrain[2]) \
            and password[constrain[0] - 1] != password[constrain[1] - 1])

filename = "day2.txt"
with open(filename, 'r') as pass_file:
      count = 0
      count2 = 0
      #file format: x-x letter: password
      for line in pass_file:
            #I'm not interester in the final '\n'
            if line[-1] == '\n':
                  line = line[0 : len(line)-1]
            #split list in it's various components
            #[x-x letter], password
            pass_list = line.split(': ')
            password = pass_list[1]
            line = pass_list[0]
            #[x-x], letter, password
            pass_list = line.split(' ')
            letter = pass_list[1]
            line = pass_list[0]
            #[x, x, letter], password
            pass_list = line.split('-')
            pass_list[0] = int(pass_list[0])
            pass_list[1] = int(pass_list[1])
            pass_list.append(letter)
            
            #---PART ONE---
            if is_pass_valid(pass_list, password):
                  count += 1

            #---PART TWO---
            if is_pass_valid2(pass_list, password):
                  count2 += 1

print(count)
print(count2)
