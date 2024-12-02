# original attempt at day 2 of advent of code https://adventofcode.com/2024/day/2
# i was able to get part 1 by myself but after spending almost the whole day trying to do part 2 i gave up and looked at other peoples answers
# that is available in part2.py

import re

# read input file (parse into list of lines to make formatting easier)
def parse_file(filename):
    f = open(filename)
    file = f.readlines()
    f.close()
    return file

# format lines for checking values
def format_lines(file):
    lines = []

    for i in file:
        # the newlines show up in the list of lines so remove those too
        x = re.split(' |\n', i)
        y = []
        for j in x:
            # avoid final line in input file
            if j != '':
                # convert strings to ints
                y.append(int(j))
        lines.append(y)
    return lines

# check that the vales are going the same direction and aren't too far apart
# also major spagetti code oops
def check_values(line):
    values = []
    safe = False
    x = prev_value = 0

    # make a new list of value - previous value
    while x < len(line):
        if x == 0:
            prev_value = line[x]
        else:
            values.append(line[x] - prev_value)
            prev_value = line[x]
        x+=1
    
    print(values)
    return values

def increase_test(x):
    increase = 0
    if x > 0:
        increase = 1
    elif x < 0:
        increase = -1
    else:
        increase = 0
    #print(increase)
    return increase

# check that the increase/decrease is the same
def check_increase(values):
    x = increase = prev_increase = 0

    #print(values)

    while x < len(values):
        # check if values are increasing or decreasing by too much (or if its 0 then its a duplicate and no change)
        if -3 <= values[x] <= 3 and values[x] != 0:
            # if its the first number set it to the previous value
            # check if its increasing or decreasing
            increase = increase_test(values[x])
                
            # check that its going the same direction as the last increase/decrease
            #print(increase, prev_increase)
            if x == 0:
                # nothing to compare to so it just sets the previous one to the current one
                prev_increase = increase
            else:
                # increase in the same direction
                if increase == prev_increase:
                    safe = True
                    prev_increase = increase
                else:
                    safe = False
                    break
                
        else:
            safe = False
            break
        x+=1
    
    #print(safe)
    return safe

# honestly idk what this is supposed to do
def janky_edge(value1, value2, value3):
    case = [value1-value3, value1-value2, value2-value3]
    wrong = 0
    if not -3 <= case[0] <= 3 or case[0] ==0:
        wrong = value2
    elif not -3 <= case[1] <= 3 or case[1] ==0:
        wrong = value3
    elif not -3 <= case[2] <= 3 or case[2] ==0:
        wrong = value1
    return wrong

def idkman(values):
    x = difference = increase = prev_increase = 0
    total_safe = unsafe = False

    print(values)

    while x < len(values):
        if x != 0:
            print(values[x-1], values[x])
            difference = values[x] - values[x-1]
            if -3 <= difference <= 3 and difference != 0:
                increase = increase_test(difference)

                #print(increase, prev_increase)
                if x==1:
                    prev_increase = increase
                else:
                    if increase == prev_increase and increase != 0:
                        total_safe = True
                        prev_increase = increase
                    else:
                        if not unsafe:
                            values.remove(janky_edge(values[x-1], values[x], values[x+1]))
                            unsafe = True
                            print("dampener used: change of increase")
                            x-=1
                        else:
                            total_safe = False
                            print("change of increase")
                            break
            else:
                if not unsafe:
                    values.remove(janky_edge(values[x-1], values[x], values[x+1]))
                    unsafe = True
                    print("dampener used: gap too big")
                    x-=1
                else:
                    total_safe = False
                    print("gap too big")
                    break
        x+=1
    
    print(values)
    print(total_safe)
    return total_safe

def idkwhatswrongwiththis(lines):
    combo = []
    x = 0

    for i in lines:
        while x < len(i):
            combo.append(i)
            x+=1
    
    #print(combo)
    print(combo)

def part1(lines):
    total_safe = 0

    for i in lines:
        values = check_values(i)
        if check_increase(values):
            total_safe+=1
    
    print("total number of safe reports is:", total_safe)

def part2(lines):
    total_safe = 0

    idkwhatswrongwiththis(lines)
    
    #print("total number of safe reports with dampener is:", total_safe)

# main code
file = parse_file("test.txt")
lines = format_lines(file)

#part1(lines)
part2(lines)