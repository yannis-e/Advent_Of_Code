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

    ### Code for processing the data ###

    last = 0
    safe = True
    
    for l in data.splitlines():
        report = l.split()
        safe = True
        for p, n in enumerate(report):
            report[p] = int(n)
        for p, n in enumerate(report):
            if p == 0:
                if report[0] < report[1]:
                    increasing = True
                if report[0] > report[1]:
                    increasing = False

            else:
                if last == n:
                    safe = False
                elif abs(last - n) > 3:
                    safe = False
                elif last < n:
                    if not increasing:
                        safe = False
                elif last > n:
                    if increasing:
                        safe = False
            last = n

        if safe == True:
            solution += 1
    ### End of processing logic ###

    return solution

# Read data from the files
inputdata = read_file("./input.txt")
testdata = read_file("./test.txt")
test_expec = 2

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