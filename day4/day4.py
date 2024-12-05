#advent of code day 4 https://adventofcode.com/2024/day/4

# first some funky stuff to make my module work
import sys
sys.path.append('../')
from commonfunc import cf

# tuple for each letter of XMAS to test for matches
xmas = ('X', 'M', 'A', 'S')
mas = ('M', 'A', 'S')

# directions for the word
directions = ([-1, -1], [-1, 0], [-1, 1],
                [0, -1], [0, 1],
                [1, -1], [1, 0], [1, 1])

# put the letters into a 2 dimensional list
def format_file(file):
    letters = []
    x = []
    
    for i in file:
        if i == "\n" or '':
            #print("newline")
            letters.append(x)
            x = []
        else:
            x.append(i)
    
    return letters

def check_word(matrix, position, direction, word):
    xmas = []
    x = 1

    print("checking", position, direction)
    xmas.append(matrix[position[0]][position[1]])
    print(0, "appended", matrix[position[0]][position[1]])
    while x < len(word):
        try:
            next_letter = [position[0]+(direction[0]*x), position[1]+(direction[1]*x)]
            if not (next_letter[0] <0 or next_letter[1] <0):
                xmas.append(matrix[next_letter[0]][next_letter[1]])
                print(x, "appended", matrix[next_letter[0]][next_letter[1]])
        except:
            print(x, "nothing to append")
            xmas.append(None)
        x+=1
    
    if xmas == list(word):
        return True
    else:
        return False

def check_word_diagonal(matrix, position, direction, word):
    xmas = []

    print("checking", position, direction)
    xmas.append(matrix[position[0]][position[1]])
    print(0, "appended", matrix[position[0]][position[1]])

    try:
        xmas.append(matrix[position[0]+direction[0]][position[1]+direction[1]])
        print(1, "appended", matrix[position[0]+direction[0]][position[1]+direction[1]])
        xmas.append(matrix[position[0]+(direction[0]*-1)][position[1]+(direction[1]*-1)])
        print(2, "appended", matrix[position[0]+(direction[0]*-1)][position[1]+(direction[1]*-1)])
    except:
        print("nothing to append")
        xmas.append(None)
    
    
    if xmas == list(word):
        return True
    else:
        return False

def check_direction(matrix, position, index, word):
    try:
        letter = matrix[position[0]][position[1]]
    except:
        letter = None
    if letter == word[index] and not (position[0] <0 or position[1] <0):
            return True
    return False

def check_direction_diagonal(matrix, position, index, word):
    try:
        letter = matrix[position[0]][position[1]]
    except:
        letter = None
    if letter == word[index] and not (position[0] <= 0 or position[1] <= 0):
            print("found diagonal", word[index])
            return True
    return False

def check_xmas(letters, word):
    matches = x = y = 0
    while x < len(letters):
        print("loop line")
        while y < len(letters[x]):
            good_dir = correct = False
            index = 0
            dir_match = []
            position = [x, y]
            letter = letters[x][y]
            print(position, letter)

            if letter == word[index]:
                index+=1
                # check the area around x
                for i in directions:
                    good_dir = check_direction(letters, [position[0]+i[0], position[1]+i[1]], index, word)
                    if good_dir:
                        dir_match.append(i)
                
                # check the directions found
                print("checking directions", dir_match)
                for i in dir_match:
                    correct = check_word(letters, position, i, word)
                    if correct:
                        print("xmas found")
                        matches+=1
            
            y+=1
        y = 0
        x+=1
    
    return matches

def check_mas(letters, word):
    matches = x = y = 0
    while x < len(letters):
        print("loop line")
        while y < len(letters[x]):
            good_dir = correct = False
            index = 0
            dir_match = []
            position = [x, y]
            letter = letters[x][y]
            print(position, letter)

            if letter == word[index]:
                index+=1
                # check the area around m
                for i in directions:
                    good_dir = check_direction_diagonal(letters, [position[0]+i[0], position[1]+i[1]], index, word)
                    if good_dir:
                        dir_match.append(i)

                for i in dir_match:
                    correct = check_word_diagonal(letters, position, i, word)
                    if correct:
                        print("xmas found")
                        matches+=1
            
            y+=1
        y = 0
        x+=1
    
    return matches

# part 1
def part1(matrix):
    word = xmas
    #print((matrix))

    matches = check_xmas(matrix, word)
    print("total XMAS:", matches)

def part2(matrix):
    word = mas

    matches = check_mas(matrix, word)
    print("total X-MAS:", matches)
    

# why do nested list comprehensions not scoped in classes
# thank you https://stackoverflow.com/questions/20136955/nested-list-comprehension-scope
def work(matrix):
    x = y = 2
    return [[b for b in a[y-1:y+2]] for a in matrix[x-1:x+2]]

class Main:
    file = cf.parse_file("test.txt")
    matrix = format_file(file)
    #print(file)
    #part1(matrix)
    part2(matrix)