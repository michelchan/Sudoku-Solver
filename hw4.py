import sys
import string

# the dictionary that will hold everything
sudokutionary = {}
# Used to refer to row name
rows = 'ABCDEF'
# Used to refer to row index
columns = '123456'
changed = True


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
def checkOne(done):
    check = ["A1", "B2", "C3", "D4", "E5", "F6"]
    for i in check:
        # cross is an array where the first element is an array of all the keys in the same row
        #                         the second element is an array of all the keys in the same column
        cross = getLine(i)
        # for every element in the row check what its value is, can be
        for z in cross[0]:
            # If there's only one option left, remove it from everything else
            if len(sudokutionary[z]) == 1:
                # for every element in the row again, remove the number it can't be
                for y in cross[0]:
                    # if the current element isn't the one its looping through, remove
                    if z != y:
                        if sudokutionary[y] != sudokutionary[y].replace(sudokutionary[z], ""):
                            sudokutionary[y] = sudokutionary[y].replace(sudokutionary[z], "")
                            done = True
                    else:
                        pass
        # for every element in the column check what its value is, can be
        for j in cross[1]:
            if len(sudokutionary[j]) == 1:
                # for every element in the column again, remove the number it can't be
                for k in cross[1]:
                    # if the current element isn't the one its looping through, remove
                    if j != k:
                        if sudokutionary[k] != sudokutionary[k].replace(sudokutionary[j], ""):
                            sudokutionary[k] = sudokutionary[k].replace(sudokutionary[j], "")
                            done = True
                    else:
                        pass
        # for every element in the box check what its value is, can be
        for j in cross[2]:
            
    return done


# Takes key and returns array with index 0 with all elements in row and index 1 with all elements in column
def getLine(key):
    row = []
    column = []
    box = []
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
    if "A" in key or "B" in key:
        if "1" in key or "2" in key or "3" in key:
            box.extend(["A1", "A2", "A3", "B1", "B2", "B3"])
        else:
            box.extend(["A4", "A5", "A6", "B4", "B5", "B6"])
    elif "C" in key or "D" in key:
        if "1" in key or "2" in key or "3" in key:
            box.extend(["C1", "C2", "C3", "D1", "D2", "D3"])
        else:
            box.extend(["C4", "C5", "C6","D4", "D5", "D6"])
    elif "E" in key or "F":
        if "1" in key or "2" in key or "3" in key:
            box.extend(["E1", "E2", "E3", "F1", "F2", "F3"])
        else:
            box.extend(["E4", "E5", "E6", "F4", "F5", "F6"])
    return [row, column, box]


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

    # Keep solving the puzzle until it is done
    while changed:
        changed = checkOne(False)
        if changed == False:
            for x in sudokutionary:
                if len(sudokutionary[x]) > 1:
                    sudokutionary[x] = sudokutionary[x][0]
                    changed = True
                    break

    printpuzzle(sudokutionary)
