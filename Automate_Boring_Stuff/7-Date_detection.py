'''TEXT
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months 
range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years;
it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and 
write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, 
and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except 
for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to 
make a reasonably sized regular expression that can detect a valid date.'''

'''PSEUDO-CODE
---regex which find dates and saves them in a list
---I split up each string in variables month, day, year:
    ---if (month==4,6,9,11) => day<=30 ok
    ---if (month==2) =>
        ---if day>29 => false 
        ---if day<29 => ok
        ---if day==29 => 
            ---leap year?
                ---if divisible by 4 
                    ---if divisible by 100 and not by 400 =>false
            => ok
    ---if ok => store in a list of strings
'''

import re
test = '32/05/2020 and 30/04/2000 and 29/02/2002 and 28/12/2020' #A casual list to test the program

date_regex=re.compile('[0-3][0-9]/[0-1][0-9]/[1-2][0-9]{3}') #regex to find dates set

res=[]
res=date_regex.findall(test) #I insert each date in res, which is a list of lists

final=[] #It will contain only the correct dates
for date in res: #I have to analyze every element of the list, to know if it's a valid date
    day, month, year=date.split('/') #multiple assignment
    day=int(day)
    month=int(month)
    year=int(year)

    if day>31:
        continue
    if month==4 or month==6 or month==9 or month==11:
        if day>30:
            continue
    if month==2:
        if day>29:
            continue
        elif day==29:
            if not year%4==0:
                continue
            elif year%4==0:
                if year%100==0 and year%400!=0:
                    continue
    final.append(date) 

#Printing final to control if the code is correct
for date in final:
    print(date)
