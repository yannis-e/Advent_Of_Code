import re

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return ""  # Return empty string if file is not found
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""  # Return empty string if there's an error reading the file

def check_xmas(line):
    count = 0

    r = r"(XMAS)|(SAMX)"
    for x in re.findall(r, line):
        count += 1

    return count

def check_diagonal(x, y, h, w, letters):
    letter_str = ""
    while True:
        letter_str += letters[y-1][x-1]
        x += 1
        y += 1
        if x >= w or y >= h:
            break
    return check_xmas(letter_str)

def main(data):
    """Processes the data and returns the result."""
    solution = 0

    w, h = len(data.splitlines()[0]), len(data.splitlines())

    letters = [[0 for x in range(w)] for y in range(h)]

    for p,l in enumerate(data.splitlines()):
        for i,n in enumerate(list(l)):
            letters[p][i] = n

    #Vertical
    for x in range(w):
        lines_str = ""
        for y in range(h):
            lines_str += letters[y][x]
        solution += check_xmas(lines_str)

    # Horizontal
    for x in range(h):
        lines_str = ""
        for y in range(w):
            lines_str += letters[x][y]
        solution += check_xmas(lines_str)

    # Diagonal
    z = 0
    y = h
    for i in range(w+(h-1)):
        while z != 0 and y != 0:
            solution += check_diagonal(z, y, h, w, letters)
            y -= 1
        while z != w:
            solution += check_diagonal(z, y, h, w, letters)
            z += 1
        


    #solution = lines_str
    return solution

# Read data from the files
inputdata = read_file("./input.txt")
testdata = read_file("./test.txt")
test_expec = 11

# Output the results by calling `main` with the data from the files
print("Test data output:")
test = main(testdata)
print(main(testdata))  # Process and print the content of test.txt

if test == test_expec:
    print("Test is correct!")
    
    print("\nInput data output:")
    print(main(inputdata))  # Process and print the content of input.txt
