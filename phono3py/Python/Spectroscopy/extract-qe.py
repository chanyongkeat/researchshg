import os
import re

# Path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through the output files from 001 to 010
for i in range(1, 11):
    # Generate the input and output filenames dynamically
    input_filename = f"Si-ph.0004.{i:03}.out"
    output_filename = f"Si-dielectric.0004.{i:03}.dat"
    
    # Full paths for input and output files
    input_filepath = os.path.join(current_dir, input_filename)
    output_filepath = os.path.join(current_dir, output_filename)
    
    # Check if the input file exists
    if not os.path.isfile(input_filepath):
        print(f"{input_filename} does not exist, skipping.")
        continue

    # Open and read the input file
    with open(input_filepath, 'r') as infile:
        lines = infile.readlines()

    # Initialize a list to store the extracted numbers
    dielectric_data = []

    # Search for the lines containing the dielectric matrix
    start_extracting = False
    for line in lines:
        if "Dielectric constant in cartesian axis" in line:
            start_extracting = True
            dielectric_data = []  # Reset data to capture only the last occurrence
        elif start_extracting:
            # Regex to match numbers separated by spaces within parentheses
            if re.match(r'\s*\(\s*[\d\.\-E]+\s+[\d\.\-E]+\s+[\d\.\-E]+\s*\)', line):
                # Extract the numbers inside parentheses
                numbers = re.findall(r"[\d\.\-E]+", line)
                dielectric_data.append(" ".join(numbers))
            elif dielectric_data:
                start_extracting = False  # Reset extraction flag to look for the next occurrence

    # Write the dielectric data to the output file if any data was extracted
    if dielectric_data:
        with open(output_filepath, 'w') as outfile:
            outfile.write("\n".join(dielectric_data))
        print(f"Last dielectric constant matrix from {input_filename} saved to {output_filename}")
    else:
        print(f"No dielectric constant matrix found in {input_filename}")
