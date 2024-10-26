import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the input file
input_file = os.path.join(current_dir, 'nbbfc.inp')

# Ensure the input file exists in the current directory
if not os.path.isfile(input_file):
    print(f"Error: '{input_file}' not found in the current directory.")
else:
    # Read the content of the original file
    with open(input_file, 'r') as file:
        file_content = file.readlines()

    # Loop to create multiple versions of the file
    for i in range(1, 4):  # Creates coord_1.in, coord_2.in, and coord_3.in
        # Create a copy of the content
        modified_content = file_content[:]
        
        # Modify the '@include 'coord.in'' line to '@include 'coord_#.in''
        for j in range(len(modified_content)):
            if "@include 'coord.in'" in modified_content[j]:
                modified_content[j] = f"  @include 'coord_{i}.in'\n"
                break  # Stop after the first match
        
        # Save the modified content to a new file with updated filename
        output_file = os.path.join(current_dir, f'nbbfc_{i}.inp')
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File '{output_file}' created successfully!")
