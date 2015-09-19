import sys
import string

# the dictionary that will hold everything
sudokutionary = {}
# Used to refer to row name
rows = 'ABCDEF'
# Used to refer to row index
columns = '123456'


# Prepares the dictionary
def setup():
    for i in rows:
        for j in columns:
            # square is the name of the square eg A1 E6
            square = i + j
            # These are all the possible numbers a square can be
            sudokutionary[square] = '123456'


# Prints out the board
def printpuzzle(dictionary):
    for i in dictionary:
        print(i, dictionary[i])


with open(sys.argv[1], 'r') as text:
    # read in file, go through each line and replace '-' with 0 and remove spaces and new lines
    filteredText = ''
    for line in text:
        filteredText += line.strip()

    # sets up the board with the values that are already there
    setup()
    for i, val in enumerate(filteredText):
        if i == '-':
            pass
        else:
            sq = (i // 6) + 65
            index = (i % 6) + 49
            # print(chr(sq), chr(index), i, val)
            c = chr(sq) + chr(index)
            sudokutionary[c] = val
    print(filteredText)
    printpuzzle(sudokutionary)
