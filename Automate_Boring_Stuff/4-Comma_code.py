'''Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
with and inserted before the last item. Your function should be able to work with any list value passed to it. Be sure to test the case 
where an empty list [] is passed to your function.'''
import copy

el=[]
last_el=''
i=0
cont=0
res=''

print('Write down the elements of the list (type "no" to end the insert mode): ')
while last_el!='end':
    last_el=input()
    if last_el!='end':
        el.append(last_el)
        cont=cont+1

if cont==0:
    print("Non hai inserito elementi.")
else:
    for i in range (0, cont):
        res=res + str(el[i])
        if i==cont-2:
            res=res + ' and '
        elif i!=cont-1:
            res=res + ', '
