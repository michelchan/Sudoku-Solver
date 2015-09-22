import sys
import string

# the dictionary that will hold everything
sudokutionary = {}
# Used to refer to row name
rows = 'ABCDEF'
# Used to refer to row index
columns = '123456'
temp = {}


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
    string = ''
    # for i in dictionary:
    #     print(dictionary[i], " ")
    for i in rows:
        for j in columns:
            # square is the name of the square eg A1 E6
            square = i + j
            # These are all the possible numbers a square can be
            string += sudokutionary[square]
            string += " "
        string += "\n"
    print(string)


# Removes option that the square cannot be
def checkAvailable():
    check = ["A1", "B2", "C3", "D4", "E5", "F6"]
    for i in check:
        # cross is an array where the first element is an array of all the keys in the same row
        #                         the second element is an array of all the keys in the same column
        cross = getLine(i)
        # for every element in the row check what its value is, can be
        for z in cross[0]:
            if len(sudokutionary[z]) == 1:
                # for every element in the row again, remove the number it can't be
                for y in cross[0]:
                    # if the current element isn't the one its looping through, remove
                    if z is not y:
                        sudokutionary[y] = sudokutionary[y].replace(sudokutionary[z], "")
        # for every element in the column check what its value is, can be
        for j in cross[1]:
            if len(sudokutionary[j]) == 1:
                # for every element in the column again, remove the number it can't be
                for k in cross[1]:
                    # if the current element isn't the one its looping through, remove
                    if j != k:
                        sudokutionary[k] = sudokutionary[k].replace(sudokutionary[j], "")


# Takes key and returns array with index 0 with all elements in row and index 1 with all elements in column
def getLine(key):
    row = []
    column = []
    # get row from first index in string
    letter = key[0]
    # get index from second index in string
    number = key[1]
    # Iterate through the dictionary, if a key is in the same row, add to array
    for j in sudokutionary:
        if letter in j:
            row.append(j)
    # Iterate through the dictionary, if key is in the same column, add to array
    for k in sudokutionary:
        if number in k:
            column.append(k)
    return [row, column]


def done():
    # goes through keys in dictionary
    for i in sudokutionary:
        # if every square on the board has only 1 option left then it is done
        if len(sudokutionary[i]) != 1:
            return False


with open(sys.argv[1], 'r') as text:
    # read in file, go through each line and replace '-' with 0 and remove spaces and new lines
    filteredText = ''
    for line in text:
        filteredText += line.strip()

    # sets up the board with the values that are already there
    filteredText = filteredText.replace(' ', '')
    setup()
    # Iterate through the text input,
    # if read in '-' then don't do anything,
    # else put that number into the dictionary
    for i, val in enumerate(filteredText):
        if val == '-':
            pass
        else:
            sq = (i // 6) + 65
            index = (i % 6) + 49
            c = chr(sq) + chr(index)
            sudokutionary[c] = val

    while not done():
        temp = sudokutionary
        checkAvailable()

    print(filteredText)
    printpuzzle(sudokutionary)
