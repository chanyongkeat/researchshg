import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through files Si-00001.out to Si-00003.out
for i in range(1, 4):
    # Define the input and output filenames with zero-padded numbers
    input_file = os.path.join(current_dir, f'Si-{i:05d}.out')
    output_file = os.path.join(current_dir, f'Si-QE-{i:05d}.out')

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist. Skipping.")
        continue

    # Read force values from the input file and multiply each value by 2
    forces = []
    with open(input_file, 'r') as file:
        for line in file:
            x, y, z = map(float, line.split())
            forces.append((x * 2, y * 2, z * 2))  # Multiply each force component by 2

    # Write forces to the new Quantum Espresso-style output file
    with open(output_file, 'w') as outfile:
        outfile.write("     Forces acting on atoms (Ry/au):\n\n")
        
        # Iterate over the forces and write them in the required format
        for idx, (x, y, z) in enumerate(forces, start=1):
            outfile.write(f"     atom {idx:4d} type  1   force = {x:15.8f} {y:15.8f} {z:15.8f}\n")

    print(f"Processed {input_file} and wrote to {output_file}")
