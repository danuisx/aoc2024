# advent of code day 3 https://adventofcode.com/2024/day/3
# did it 1st try today B)

import re

# parse the input file (basically the same as every other day)
def parse_file(filepath):
    f = open(filepath)
    file = f.read()
    f.close()
    return file

# make a list of all the numbers to be multiplied
def format_file(file, dodont):
    mult_list = []

    # do/don't is for part 2
    if dodont:
        enabled = True

        # return a list of all mul() operations and any do()/don't() operations
        formatted = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don[']t\(\))", file)
        
        # enable/disable the adding of multiplication numbers depending on the do/don't operation
        for i in formatted:
            if re.search("(do\(\))", str(i)):
                enabled = True
            elif re.search("(don[']t\(\))", str(i)):
                enabled = False
            elif re.search("(mul\([0-9]{1,3},[0-9]{1,3}\))", str(i)) and enabled:
                # basically removes anything that isn't a number (some extra characters since the do/don't are also checked above)
                x = re.split("mul\(|[()',]|\s", str(i))
                # remove empty brackets
                x = list(filter(None, x))
                mult_list.append(x)
    else:
        # return a list of all mul() operations
        formatted = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))", file)

        # get just the numbers from the string and make a list to put into the mult_list
        for i in formatted:
            x = re.split("mul\(|,|\)", i)
            x = list(filter(None, x))
            mult_list.append(x)
        
    # since the numbers are considered strings we need to convert to ints for multiplication purposes
    mult_list = list_to_int(mult_list)

    #print(formatted)
    #print(mult_list)
    return mult_list

# goes through each item in two-dimensional mult_list and converts it from string to int
def list_to_int(mult_list):    
    y = z = 0
    while y < len(mult_list):
        while z < len(mult_list[y]):
            mult_list[y][z] = int(mult_list[y][z])
            z+=1
        z = 0
        y+=1

    return mult_list

# multiplies the two values in each list in the mult_list list
def multiply_list(mult_list):
    total = 0
    for i in mult_list:
        total+= i[0] * i[1]
        #print(total)
    
    return total

def part1(file):
    mult_list = format_file(file, False)
    print("the total sum of the multiplication is:", multiply_list(mult_list))

def part2(file):
    mult_list = format_file(file, True)
    print("the total sum of the multiplication with do/don't enabled is:", multiply_list(mult_list))

# main code

file = parse_file("input.txt")
part1(file)
part2(file)