# make my life a bit easier by not repeating the same functions everyday

# parse the input file
def parse_file(filepath):
    f = open(filepath)
    file = f.read()
    f.close()
    return file