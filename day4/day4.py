#advent of code day 4 https://adventofcode.com/2024/day/4

# first some funky stuff to make my module work
import sys
sys.path.append('../')
from commonfunc import cf

# tuple for each letter of XMAS to test for matches
word = ('X', 'M', 'A', 'S')

# directions for the word
directions = ([-1, -1], [-1, 0], [-1, 1],
                [0, -1], [0, 0], [0, 1],
                [1, -1], [1, 0], [1, 1])

# put the letters into a 2 dimensional list
def format_file(file):
    letters = []
    x = []
    y = 0
    
    for i in file:
        if i == "\n":
            #print("newline")
            letters.append(x)
            x = []
        else:
            x.append(i)
    
    return letters

def match_letter(matrix, index):
    x = y = 0

    while x < len(matrix):
        while y < len(matrix[x]):
            if matrix[x][y] == word[index]:
                print("match", index)
                return True, [x, y]
            y+=1
        y = 0
        x+=1

    return False, [0, 0]

def check_xmas(letters):
    index = matches = x = y = 0
    correct = False
    while x < len(letters):
        print("loop line")
        while y < len(letters[x]):
            print(letters[x][y])
            if letters[x][y] == word[index]:
                print("match", index)
                letter_index = [x, y]
                correct = True
                index+=1

                while index < 4 and correct:
                    print("help", index)
                    subletters = [x[(letter_index[0]-1):(letter_index[0]+2)] for x in letters[(letter_index[1]-1):(letter_index[1]+2)] if x]
                    print(letter_index, subletters)
                    correct, letter_index = match_letter(subletters, index)
                    index+=1

                if correct:
                    matches+=1
                    correct = False
            index = 0
            y+=1
        y = 0
        x+=1
    
    return matches

def check_direction(matrix, position, index, direction):
    x = 0

    if direction is not None:
        print("direction not none")
        letter = matrix[position[0]+direction[0]][position[1]+direction[1]]
        if letter == word[index] and letter is not None:
                print("it worked again")
                return True, [position[0]+direction[0], position[1]+direction[1]], [direction[0], direction[1]]
    else:
        while x < len(directions):
            letter = matrix[position[0]+directions[x][0]][position[1]+directions[x][1]]
            print("match direction", letter)
            if letter == word[index] and letter is not None:
                print("it worked")
                return True, [position[0]+directions[x][0], position[1]+directions[x][1]], [directions[x][0], directions[x][1]]
            x+=1
    
    return False, [0,0], None

def check_xmas2(letters):
    index = matches = x = y = 0
    correct = False
    while x < len(letters):
        print("loop line")
        while y < len(letters[x]):
            print(letters[x][y])
            if letters[x][y] == word[index]:
                print("match", index)
                letter_index = [x, y]
                correct = True
                index+=1
                direction = None

                while index < 4:
                    print("help", index)
                    #subletters = [x[(letter_index[0]-1):(letter_index[0]+2)] for x in letters[(letter_index[1]-1):(letter_index[1]+2)] if x]
                    #print(letter_index, subletters)
                    correct, letter_index, direction = check_direction(letters, letter_index, index, direction)
                    index+=1

                if correct:
                    print("added match")
                    matches+=1
                    correct = False
            index = 0
            y+=1
        y = 0
        x+=1
    
    return matches

def new_check_direction(matrix, position, direction, index):
    letter = matrix[position[0]+direction[0]][position[1]+direction[1]]
    if letter == word[index] and letter is not None:
            print("it worked again", letter)
            return True, [position[0]+direction[0], position[1]+direction[1]], direction
    return False, position, None

def new_check_xmas(letters):
    index = matches = x = y = z = 0
    correct = False
    while x < len(letters):
        print("loop line")
        while y < len(letters[x]):
            print(letters[x][y])
            if letters[x][y] == word[index]:
                print("match", index)
                letter_index = [x, y]
                correct = True
                index+=1
                direction = None

                while z < len(directions):
                    correct, letter_index, direction = new_check_direction(letters, letter_index, directions[z], index)
                    if direction is not None:
                        index+=1
                        break
                    z+=1
                
                while index < len(word) and correct:
                    correct, letter_index, direction = new_check_direction(letters, letter_index, direction, index)


                if correct:
                    print("added match")
                    matches+=1
                    correct = False
            index = 0
            y+=1
        y = 0
        x+=1
    
    return matches

# part 1
def part1(file):
    matrix = format_file(file)

    matches = new_check_xmas(matrix)
    print("total XMAS:", matches)

# why do nested list comprehensions not scoped in classes
# thank you https://stackoverflow.com/questions/20136955/nested-list-comprehension-scope
def work(matrix):
    x = y = 2
    return [[b for b in a[y-1:y+2]] for a in matrix[x-1:x+2]]

class Main:
    file = cf.parse_file("test.txt")
    part1(file)