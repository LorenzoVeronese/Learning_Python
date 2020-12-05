"""
PSEUDOCODE
put each line (number) in a list
slide the list to find fitted sums
"""

filename = "day1.txt"
with open(filename, 'r') as year_file:
      years = []
      for line in year_file:
            years.append(int(line))

#finish: flag variable to print only one product (in case of more 
# than one couple fitting the constraint)
finish = 0
for year1 in years:
      for year2 in years:
            if year1 + year2 == 2020:
                  print(year1 * year2)
                  finish = 1
                  break
      if finish:
            break