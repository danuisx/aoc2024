# advent of code day 1
# https://adventofcode.com/2024/day/1

import re

# parse input file
def parse_lists(file, list1, list2):
    count = 0
    #regex file splitter for space between values/newlines
    splitFile = re.split('   |\n', file)

    #split values into the lists (also cast them to ints for later)
    for i in splitFile:
        count+=1
        if (count%2 == 0):
            list2.append(int(i))
        else:
            list1.append(int(i))

#mergesort stuff (basically just https://www.w3schools.com/dsa/dsa_algo_mergesort.php bc i forgor sorting algorithms X-X)
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def mergesort(list):
    if len(list) <=1:
        return list
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    sleft = mergesort(left)
    sright = mergesort(right)

    return merge(sleft, sright)

# actually getting the difference of the two lists
def list_distance(list1, list2):
    distance = total_dist = 0
    i = 0
    
    while i < len(list1):
        distance = abs(list1[i] - list2[i])
        total_dist += distance
        i+=1
    
    return total_dist

# function for part 1 of the question (find the total distance between each list)
def part1(list1, list2):
    list1 = mergesort(list1)
    list2 = mergesort(list2)
    result = list_distance(list1, list2)
    print("total distance is:", result)

# function for part 2 of the question (similarity score)
def part2(list1, list2):
    count = total = 0

    for i in list1:
        for j in list2:
            if i == j:
                count+=1
        total += i * count
        count = 0
    
    print("similarity score is:", total)

# main code starts here
list1, list2 = [], []
f = open("input.txt")
file = f.read()
f.close()
parse_lists(file, list1, list2)

part1(list1, list2)
part2(list1, list2)
