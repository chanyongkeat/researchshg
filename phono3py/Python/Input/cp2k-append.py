import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the template input file
input_file = os.path.join(current_dir, 'nbbfc.inp')

# Ensure the input file exists in the current directory
if not os.path.isfile(input_file):
    print(f"Error: '{input_file}' not found in the current directory.")
else:
    # Read the content of the original file
    with open(input_file, 'r') as file:
        file_content = file.readlines()

    # Loop to create 3 versions of the file
    for i in range(1, 4):
        # Create a zero-padded number for the file names
        padded_num = f"{i:05d}"
        
        # Create a copy of the content
        modified_content = file_content[:]
        
        # Update the '@include 'coord.in'' line
        for j in range(len(modified_content)):
            if "@include 'coord.in'" in modified_content[j]:
                modified_content[j] = f"  @include 'coord-{padded_num}.in'\n"
                break  # Stop after the first match

        # Update the 'PROJECT NBBFC' line within the &GLOBAL section
        for j in range(len(modified_content)):
            if "PROJECT NBBFC" in modified_content[j]:
                modified_content[j] = f"  PROJECT NBBFC-supercell-{padded_num}\n"
                break  # Stop after updating the first PROJECT line
        
        # Save the modified content to a new file with the updated filename
        output_file = os.path.join(current_dir, f'NBBFC-supercell-{padded_num}.inp')
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File '{output_file}' created successfully!")
