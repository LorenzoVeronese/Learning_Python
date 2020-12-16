"""
---PART ONE---
"""
"""
PSEUDOCODE
put first lines into a dictionary {field : ((left border 1, right border 1),
                                                (left border 2, right border 2))}
make comparisons
"""

import re

def mk_fields(filename):
      with open(filename, 'r') as fd:
            fields_dict = {}
            for line in fd:
                  if line == '\n':
                        break

                  #get field as key
                  field_name = re.findall(r'^[^:]*', line)
                  
                  #get numbers
                  borders = re.findall(r'\d+', line)
                  fields_dict[field_name[0]] = ((int(borders[0]), int(borders[1])), \
                        (int(borders[2]), int(borders[3])))
      
      return fields_dict

def compare(filename, fields_dict):
      with open(filename, 'r') as fd:
            numbers = []
            start = False
            result = 0
            """
            #I need to create another dictionary to make corrispondences
            #between key and index: {index : key}
            index_key = {}
            i = 0
            for key in fields_dict.keys():
                  index_key[i] = key
                  i += 1
            """
            for line in fd:        
                  if start:
                        numbers = re.findall(r'\d+', line)
                        for number in numbers:
                              count = 0
                              for borders in fields_dict.values():
                                    for border in borders:
                                          if int(number) >= border[0] and int(number) <= border[1]:
                                                count = 1
                                                break
                                    if count == 1:
                                          break
                              if count == 0:
                                    result += int(number)
                  if line == 'nearby tickets:\n':
                        start = True
                        
      return result
                  
filename = "day16.txt"
fields_dict = mk_fields(filename)
print(compare(filename, fields_dict))