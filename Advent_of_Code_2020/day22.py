"""
---PART ONE---
"""

def parse(fd):
    decks = fd.read().rstrip().split('\n\n')
    deck1, deck2 = map(str.splitlines, decks)
    
    # drop first element (which is the string 'Player x:')
    deck1 = deck1[1:]
    deck2 = deck2[1:]

    for i in range(len(deck1)):
        deck1[i] = int(deck1[i])
        deck2[i] = int(deck2[i])

    return deck1, deck2


def play(deck1, deck2):
    while 1:
        if len(deck1) == 0:
            return deck2
        elif len(deck2) == 0:
            return deck1

        if deck1[0] > deck2[0]:
            deck1.append(deck1[0])
            deck1.append(deck2[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])
        else:
            deck2.append(deck2[0])
            deck2.append(deck1[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])
    

def find_score(deck):
    result = 0
    deck.reverse()
    for i, card in enumerate(deck):
        result += card * (i + 1)
    
    return result


fd = open("day22.txt")
deck1, deck2 = parse(fd)
final_deck = play(deck1, deck2)
print(final_deck)
print(find_score(final_deck))