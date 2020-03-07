'''Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table 
with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, 
the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    len_table=[]
    for i in range(len(table[0])): #I've to take elements of the same position from different string
        lenght=0
        for j in range(len(table)):
            if len(table[j][i])>lenght:
                lenght=len(table[j][i])
        len_table.append(lenght)       
    #Now I've the list len_table which contains all the maximum lenghts of each line

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(str(table[j][i].rjust(len_table[i])), end=' ')
        print()

print_table(table_data)

'''Edit. I read badly the text of the exercise, so I made the program calcolate the space in lines, not in colums. Anyways the solution
very similar.'''
