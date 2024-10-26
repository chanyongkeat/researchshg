import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Full paths for input and output files
input_filename = 'cp2k.inp'
output_filename = 'output.txt'

# Define paths to cp2k.inp and output.txt using the current directory
cp2k_inp_file = os.path.join(current_dir, input_filename)
output_file = os.path.join(current_dir, output_filename)

# Open cp2k.inp for reading
with open(cp2k_inp_file, 'r') as file:
    cp2k_content = file.readlines()

# Read the output.txt file with numbers
with open(output_file, 'r') as file:
    output_lines = file.readlines()

# For every three rows in output.txt, create a new cp2k_#.out file
for i in range(0, len(output_lines), 3):
    # Modify cp2k content with the new lines
    new_cp2k_content = cp2k_content[:]
    new_cp2k_content[1] = f"  A {output_lines[i].strip()}\n"
    new_cp2k_content[2] = f"  B {output_lines[i+1].strip()}\n"
    new_cp2k_content[3] = f"  C {output_lines[i+2].strip()}\n"
    
    # Write to coord_#.out file
    output_cp2k_file = os.path.join(current_dir, f'coord_{i//3 + 1}.in')
    with open(output_cp2k_file, 'w') as file:
        file.writelines(new_cp2k_content)

print("All coord_#.in files created successfully!")
