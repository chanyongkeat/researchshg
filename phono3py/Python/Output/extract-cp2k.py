import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through the 3 files
for i in range(1, 4):
    # Generate the input and output filenames dynamically
    input_filename = f"Si-supercell-{i:05d}-forces-1_0.xyz"
    output_filename = f"Si-{i:05d}.out"
    
    # Define the full path for the input and output files
    input_file = os.path.join(current_dir, input_filename)
    output_file = os.path.join(current_dir, output_filename)

    # Check if the input file exists before processing
    if not os.path.exists(input_file):
        print(f"File {input_filename} not found, skipping...")
        continue

    # Open the input file and read the data
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Flag to start extracting forces once "ATOMIC FORCES" is found
        extract_forces = False

        for line in infile:
            # Check for the start of the atomic forces section
            if "ATOMIC FORCES in [a.u.]" in line:
                extract_forces = True
                continue  # Skip the header line
            if extract_forces and line.strip().startswith("#"):
                continue  # Skip the column header line starting with '#'
            if extract_forces and "SUM OF ATOMIC FORCES" in line:
                continue  # Skip the line with 'SUM OF ATOMIC FORCES'
            if extract_forces and line.strip():
                try:
                    # Split the line into parts and extract the X, Y, Z columns
                    parts = line.split()
                    x, y, z = parts[3], parts[4], parts[5]
                    # Write the formatted output to the new file
                    outfile.write(f"{x:>15} {y:>15} {z:>15}\n")
                except IndexError:
                    continue  # Skip lines that don't contain the required data

    print(f"Atomic forces from {input_filename} have been extracted and saved to {output_filename}")
