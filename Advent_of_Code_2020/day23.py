"""
---PART ONE---
"""
"""
PSEUDOCODE
for 100 steps:
    index 0 is the current cup
    index 1, 2, 3 are the three clockwise cups
    find the destination cup
    put the three cups after the destination cup
    take index 0 and put at the end
"""

def play(cups):
    cups = list(cups)
    for i in range(0, len(cups)):
        cups[i] = int(cups[i])

    lenght = len(cups)
    for i in range(0, 100):
        curr = cups[0]
        aux = cups[1: 4] # auxiliar group of 3 cups

        dest = curr - 1
        while dest in aux or dest == 0:
            dest -= 1
            if dest <= 0:
                dest = lenght

        for el in reversed(aux):
            cups.insert(cups.index(dest) + 1, el)
            cups.remove(el)
        # cups.remove(dest)
        # cups.insert(1, dest)
        
        # I represent a list so that the current element is
        # always at the start
        cups.remove(curr)
        cups.append(curr)
    
    return cups


def print_from(to_print, i):
    from_i = ''
    for el in res[res.index(i) + 1:]:
        from_i += str(el)
    for el in res[:res.index(i)]:
        from_i += str(el)
    
    print(from_i)


starting = '469217538'
res = play(starting)
print_from(res, 1)