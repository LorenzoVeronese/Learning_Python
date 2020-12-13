"""
PART ONE
"""
"""
PSEUDOCODE
for every id of the file
      sum it with himself until it becomes upper then the time I can take the bus
      make a difference between the last one (which was upper) and the time
      memorize at each loop the best number
"""

filename = "day13.txt"
with open(filename, 'r') as fd:
      #first line
      available = fd.readline()
      available = available[0 : len(available) - 1]
      available = int(available)
      
      #second line
      second = fd.readline()
      second = second.split(',')
      
      #this drops all occurrences of x in the list
      second = list(filter(lambda d: d != 'x', second))
      
      #starting values
      best_id = int(second[0])
      best_diff = int(second[0])
      for bus_id in second:
            bus_id = int(bus_id)
            curr = bus_id
            while curr < available:
                  curr += bus_id
            if (curr - available) < best_diff:
                  best_id = bus_id
                  best_diff = curr - available
                  
print(best_id, best_diff, best_id * best_diff)