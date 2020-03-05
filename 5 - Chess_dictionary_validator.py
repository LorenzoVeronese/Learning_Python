'''TEXT 
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', 
'3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary 
argument and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white king. Each player can only have at most 
16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t 
be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 
'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted 
in an improper chess board.
Edit: I generalized the problem, controlling all types of piece.'''

'''SOLUTION
To know if the positions are right, I slice strings in two parts: number (from 1 to 8) and letter (from a to h) and 
   I check 
To know if the pedins are of a right number, I use dicionary to consider the number of each piece, controlling 
    if they exceed the maximum value. When I put them in the dictionary, I slice the string controlling if the first
    letter is a "w" or a "b". One dictionary stores blacks ones, the other white ones.'''

'''ord() da il valore ascii della lettera'''

#INITIALIZATION
res=True
dictionary={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
btemp={'bpawn':0, 'bknight':0, 'bbishop':0, 'brook':0, 'bqueen':0, 'bking':0}
wtemp = {'wpawn': 0, 'wknight': 0, 'wbishop': 0, 'wrook': 0, 'wqueen': 0, 'wking': 0}

#ON BOARD?
for key in dictionary.keys():
    if int(key[0])<0 or int(key[0])>9:
        res=False
    if ord(key[1])<ord('a') or ord(key[1])>ord('h'):
        res=False

#PIECES: written in the right way? Right quantity?
#Creating temp dictionaries
for value in dictionary.values():
    if value[0]!='b' and value[0]!='w':
        res=False
    elif value[0]=='b':
        btemp[value]=btemp[value]+1
    elif value[0]=='w':
        wtemp[value]=wtemp[value]+1
#Controlling black items' values
for item in btemp.items():
    if item[0]=='bpawn' and item[1]>8:
        res=False
    elif item[0]=='bknight' and item[1]>2:
        res=False
    elif item[0]=='bbshop' and item[1]>2:
        res=False
    elif item[0]=='brook' and item[1]>2:
        res=False
    elif item[0]=='bqueen' and item[1]>2:
        res=False
    elif item[0]=='bking' and item[1]>2:
        res=False
#Controlling white items' values
for item in wtemp.items():
    if item[0] == 'wpawn' and item[1] > 8:
        res = False
    elif item[0] == 'wknight' and item[1] > 2:
        res = False
    elif item[0] == 'wbshop' and item[1] > 2:
        res = False
    elif item[0] == 'wrook' and item[1] > 2:
        res = False
    elif item[0] == 'wqueen' and item[1] > 2:
        res = False
    elif item[0] == 'wking' and item[1] > 2:
        res = False

#Printing the result
if res==True:
    print("It's ok!")
else:
    print("Someone cheated!")
