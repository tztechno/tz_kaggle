# Open the file in read mode
with open('your_file.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        # Process each line as needed
        print(line.strip())  # strip() is used to remove the newline character at the end of each line
