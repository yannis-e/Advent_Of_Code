import os

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

    list_l = []
    list_r = []
    distance_list = []

    for line in data.splitlines():
        split_line = line.split("   ")
        list_l.append(int(split_line[0]))
        list_r.append(int(split_line[1]))

    for n in list_l:
        sim_score = 0
        for i in list_r:
            if n == i:
                sim_score+=1
        solution+=n*sim_score

    return solution

# Read data from the files
inputdata = read_file("./input.txt")
testdata = read_file("./test.txt")
test_expec = 31

# Output the results by calling `main` with the data from the files
print("Test data output:")
test = main(testdata)
print(main(testdata))  # Process and print the content of test.txt

if test == test_expec:
    print("Test is correct :)")
    
    print("\nInput data output:")
    print(main(inputdata))  # Process and print the content of input.txt
else:
    print("Test incorect :(")