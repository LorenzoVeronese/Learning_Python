"""
---PART ONE---
"""

def find_loop(key, subj):
    loop_size = 1
    curr = subj
    while curr != key:
        curr = (curr * subj) % 20201227
        loop_size += 1
    
    return loop_size


def find_encr(subj, loop_size):
    curr = subj
    for i in range(loop_size - 1):
        curr = (curr * subj) % 20201227

    return curr


# input
card_key = 17607508
door_key = 15065270

subj = 7
card_loop = find_loop(card_key, subj)
# door_loop = find_loop(door_key, subj)

encr_key = find_encr(door_key, card_loop)
print(encr_key)