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
    solution = ""

    array = [row.split() for row in data]
    print(array)

    x_pos = 0
    y_pos = 0

    for y, l in enumerate(array):
        for x, n in enumerate(y):
            if n == "^":
                x_pos = x
                y_pos = y

    end = False
    di = "up" 
    
    while not end:
        if di == "up":
            if l:
                pass

    solution = str(x_pos) + str(y_pos)

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
