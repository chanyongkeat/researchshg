import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the energy.out file
energy_file = os.path.join(current_dir, 'energy.out')

# Read energy values from energy.out
with open(energy_file, 'r') as file:
    energy_values = [float(line.strip()) * 2 for line in file]  # Multiply each energy by 2

# Write each value to the corresponding output file in Quantum Espresso format
for idx, energy in enumerate(energy_values):
    # Generate the output filename based on the index
    output_filename = os.path.join(current_dir, f'Dst01_{idx+1:02d}.out')
    
    # Write the energy value in the desired format
    with open(output_filename, 'w') as output_file:
        output_file.write(f"!    total energy = {energy}\n")

    print(f"Energy value {energy} written to {output_filename}")
