"""
---PART ONE---
I used recursive functions: obviously an itelative solution would have been 
better, but I wanted to excercise on recursivity
"""
"""
PSEUDOCODE bisection method (recursively)
count lines and rows
for each line of the file
      find_row
      find_column
      get_value
      check if the value is the best
"""
import math

def count_rows(filename):
      """
      PARAMETHER
      filename: string, containing the file's name
      RETURN
      number of rows
      """
      with open(filename, 'r') as air_map:
            line = air_map.readline()
      return line.count('F') + line.count('B')

def count_columns(filename):
      """
      PARAMETHER
      filename: string, containing the file's name
      RETURN
      number of columns
      """
      with open(filename, 'r') as air_map:
            line = air_map.readline()
      return line.count('L') + line.count('R')

def find_row(line, rows):
      """
      PARAMETHERS
      line: list, containing the line of the file
      rows: list, containing the starting end the ending row numbers
      RETURN
      number of the seat's row

      EXECUTION
      row_seat = upper number - lower number
      base case, void line
            return upper number
      else
            if F
                  divide the upper number
            elif B
                  divide the lower number
      return row_seat
      """    
      if line == '':
           return rows[1]
      else:
            #print(line)
            if line[0] == 'F':
                  rows[1] = int((rows[1] + rows[0]) / 2)
                  row_seat = find_row(line[1 : len(line)], rows)
            elif line[0] == 'B':
                  rows[0] = int((rows[1] + rows[0]) / 2)
                  row_seat = find_row(line[1 : len(line)], rows)
      return row_seat


def find_column(line, columns):
      """
      PARAMETHERS
      line: list, containing the line of the file
      columns: list, containing the "lefter" (lower) and the "righter" (upper) columns
      RETURN
      number of the seat's column

      EXECUTION
      column_seat = upper number - lower number
      base case, void line
            return upper number
      else
            if R
                  divide the upper number
            elif L
                  divide the lower number
      return column_seat
      """
      if line == '':
            return columns[1]
      else:
            if line[0] == 'L':
                  columns[1] = int((columns[1] + columns[0]) / 2)      
                  column_seat = find_column(line[1: len(line)], columns)
            elif line[0] == 'R':
                  columns[0] = int((columns[1] + columns[0]) / 2)
                  column_seat = find_column(line[1: len(line)], columns)
      return column_seat

filename = "day5.txt"
row_number = count_rows(filename)
column_number = count_columns(filename)
with open(filename, 'r') as air_map:
      best_value = 0
      for c_line in air_map:
            if c_line[len(c_line)-1] == '\n':
                  line = c_line[0 : len(c_line)-1]
            else:
                  line = c_line
            value = find_row(line[0 : (len(line)-column_number)], [0, 2 ** row_number-1]) * 8 \
                  + find_column(line[row_number : len(line)], [0, 2 ** column_number-1])
            if value > best_value:
                  best_value = value

print(best_value)
