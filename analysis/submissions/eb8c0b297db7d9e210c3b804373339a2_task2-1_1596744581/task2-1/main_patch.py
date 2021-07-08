# Example code, write your program here

# Import regular expression
import re

# Filename definition
inputFile = 'data.csv'

# Output file definition
outputFile = 'output/output.csv'

# Open input file
with open(inputFile, 'r') as f:
    # Open output file
    with open(outputFile, 'w') as w:
        # Read lines
        lines = f.readlines()

        # Loop over lines
        for line in lines:
            # Split line by comma
            split_line = re.split(',+', line)

            # Remove first and last term
            split_line = split_line[1:-1]

            # Output line
            output_line = ','.join(split_line)

            # Print line
            print(output_line)

            # Add new line
            output_line += '\n'

            # Write line
            w.write(output_line)


