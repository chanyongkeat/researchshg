import os
import re

# Path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Full paths for input and output files
input_filename = 'input.txt'
output_filename = 'output.txt'

input_filepath = os.path.join(current_dir, input_filename)
output_filepath = os.path.join(current_dir, output_filename)


# Constant to multiply each value/ celldm(1) value from QE_elastic file
multiplier = 4.4799680726515998

# Read the input file
with open(input_filepath, 'r') as file:
    data = file.read()

# Regular expression to capture the numbers after V1, V2, V3
pattern = r'V\d\s--=>\s+([-]?\d+\.\d+)\s+([-]?\d+\.\d+)\s+([-]?\d+\.\d+)'

# Find all matches in the data
matches = re.findall(pattern, data)


# Open output file for writing the extracted and modified results
with open(output_filepath, 'w') as outfile:
    for match in matches:
        # Multiply each value by the multiplier
        modified_values = [float(num) * multiplier for num in match]
        
        # Format the modified numbers and write them to the output file
        outfile.write(f'{modified_values[0]:>15.10f} {modified_values[1]:>15.10f} {modified_values[2]:>15.10f}\n')

print(f"Data has been saved to {output_filepath}")
