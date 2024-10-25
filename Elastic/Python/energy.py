import os
import glob
import re

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Use glob to find all CP2K output files with the pattern cp2k_*.out
input_files = glob.glob(os.path.join(current_dir, 'cp2k_*.out'))

# Sort the files numerically by extracting the numbers from filenames
input_files.sort(key=lambda f: int(re.search(r'cp2k_(\d+).out', f).group(1)))

# Define the path for the output file where energies will be saved
output_file = os.path.join(current_dir, 'energy.out')

def extract_last_cp2k_energy(output_file):
    energy = None
    with open(output_file, 'r') as file:
        for line in file:
            if 'Total energy:' in line:
                energy = float(line.split()[-1])  # Update with each occurrence
    return energy

if __name__ == "__main__":
    energies = []

    # Extract last total energy from each CP2K output file found by glob
    for input_file in input_files:
        last_total_energy = extract_last_cp2k_energy(input_file)
        if last_total_energy is not None:
            energies.append(last_total_energy)
        else:
            print(f"Total energy not found in {input_file}")
    
    # Write all energy values to energy.out, one per line
    with open(output_file, 'w') as f:
        for energy in energies:
            f.write(f"{energy}\n")
    
    print(f"Energy values written to {output_file}")
