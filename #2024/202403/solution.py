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

def main(data):
    """Processes the data and returns the result."""
    solution = 0
    
    mult_enable = True

    for s in [match for group in re.findall(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", data) for match in group if match]:
        if "mul" in s and mult_enable:
            mult = 1
            for n in re.findall("([0-9]+)", s):
                mult *= int(n)
            solution += mult
        if "do" in s:
            mult_enable = True
        if "don't" in s:
            mult_enable = False

    return solution

# Read data from the files
inputdata = read_file("./input.txt")
testdata = read_file("./test.txt")
test_expec = 48

# Output the results by calling `main` with the data from the files
print("Test data output:")
test = main(testdata)
print(main(testdata))  # Process and print the content of test.txt

if test == test_expec:
    print("Test is correct!")
    
    print("\nInput data output:")
    print(main(inputdata))  # Process and print the content of input.txt
