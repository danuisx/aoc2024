# i couldn't figure out how to do part 2 so i checked the subreddit
# helped by the python answers at https://www.reddit.com/r/adventofcode/comments/1h4ncyr/2024_day_2_solutions/
# especially https://www.reddit.com/r/adventofcode/comments/1h4ncyr/comment/m027ef5/

import re

tolerance = (1,2,3)

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

def decreasing(line):
    x = 1
    while x < len(line):
        if line[x-1] - line[x] not in tolerance:
            return False
        else:
            x+=1
    return True

def dampener_descreasing(line):
    x = 1
    while x < len(line):
        if line[x-1] - line[x] not in tolerance:
            pop_this = decreasing(line[:x] + line[x+1:])
            pop_prev = decreasing(line[:x-1] + line[x:])
            return pop_this or pop_prev
        x+=1
    return True

def part1(report):
    total_safe = 0

    for line in report:
        if decreasing(line) or decreasing(line[::-1]):
            total_safe+=1
    
    return total_safe

def part2(report):
    total_safe = 0

    for line in report:
        if dampener_descreasing(line) or dampener_descreasing(line[::-1]):
            total_safe+=1
    
    return total_safe

# main code

file = parse_file('test.txt')
report = format_lines(file)

print("Number of safe reports:", part1(report))
print("Number of safe reports with dampener:", part2(report))