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

def check_safe(data: list):
    le = len(data)
    
    if data[0] < data[1]:
        increasing = True
    if data[1] > data[2]:
        increasing = False

    for p in range(0,le-1):
        cur = data[p] # Current Character
        nex = data[p+1] # Next Character
        if cur == nex:
            pass
        if abs(cur-nex) > 3:
            pass
        elif cur < nex:
            if not increasing:
                pass 
        elif cur > nex:
            if increasing:
                pass


def main(data):
    """Processes the data and returns the result."""
    solution = 0

    ### Code for processing the data ###
    
    for l in data.splitlines():
        report = l.split()
        check_safe(report)


    ### End of processing logic ###

    return solution

# Read data from the files
inputdata = read_file("./input.txt")
testdata = read_file("./test.txt")
test_expec = 4

# Output the results by calling `main` with the data from the files
print("Test data output:")
test = main(testdata)
print(main(testdata))  # Process and print the content of test.txt

if test == test_expec:
    print("Test is correct!")
    
    print("\nInput data output:")
    print(main(inputdata))  # Process and print the content of input.txt
else:
    print("Test incorect")