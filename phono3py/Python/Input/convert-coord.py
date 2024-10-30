import os

# Conversion factor from Bohr to Angstrom
bohr_to_angstrom = 0.5291772086

def convert_qe_to_cp2k(qe_file, cp2k_file):
    """
    Convert cell parameters and atomic positions from QE format to CP2K format.
    This will write both &CELL and &COORD sections to the CP2K file.
    """
    # Open the Quantum Espresso input file (qe.in) and read the CELL_PARAMETERS
    with open(qe_file, 'r') as file:
        lines = file.readlines()

    # Find the CELL_PARAMETERS line and extract the parameters
    cell_parameters_start = False
    atomic_positions_start = False
    cell_params = []
    atomic_positions = []

    for line in lines:
        stripped_line = line.strip()

        # Skip comment lines and empty lines
        if stripped_line.startswith('!') or stripped_line.startswith('#') or len(stripped_line) == 0:
            continue

        # Start reading CELL_PARAMETERS section
        if 'CELL_PARAMETERS' in stripped_line:
            cell_parameters_start = True
            continue

        # Stop reading CELL_PARAMETERS section if an invalid line is encountered
        if cell_parameters_start:
            try:
                cell_params.append([float(x) for x in stripped_line.split()])
            except ValueError:
                cell_parameters_start = False
                continue

        # Start reading ATOMIC_POSITIONS section
        if stripped_line.startswith("ATOMIC_POSITIONS crystal"):
            atomic_positions_start = True
            continue
        
        # Stop reading ATOMIC_POSITIONS section when a line does not match expected format
        if atomic_positions_start:
            if len(stripped_line.split()) < 4:
                break  # Stop reading atomic positions if we encounter a malformed line
            atomic_positions.append(stripped_line)

    # Convert the cell parameters from Bohr to Angstrom
    cell_params_angstrom = [[val * bohr_to_angstrom for val in row] for row in cell_params]

    # Open the CP2K input file (cp2k.inp) and write both CELL and COORD sections
    with open(cp2k_file, 'w') as file:
        # Write CELL section
        file.write("&CELL\n")
        file.write(f"  A {cell_params_angstrom[0][0]:.12f} {cell_params_angstrom[0][1]:.12f} {cell_params_angstrom[0][2]:.12f}\n")
        file.write(f"  B {cell_params_angstrom[1][0]:.12f} {cell_params_angstrom[1][1]:.12f} {cell_params_angstrom[1][2]:.12f}\n")
        file.write(f"  C {cell_params_angstrom[2][0]:.12f} {cell_params_angstrom[2][1]:.12f} {cell_params_angstrom[2][2]:.12f}\n")
        file.write("  PERIODIC XYZ  # Apply periodic boundary conditions in all directions\n")
        file.write("&END\n\n")

        # Write COORD section
        file.write("&COORD\n")
        file.write("SCALED\n")  # Assuming positions are in crystal (scaled) format.
        for position in atomic_positions:
            file.write(f"  {position}\n")
        file.write("&END\n")
    
    print(f"Conversion complete. Output written to {cp2k_file}")

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input and output filenames as strings
input_file = os.path.join(current_dir, 'supercell.in')
output_file = os.path.join(current_dir, 'coord.in')

# Call the conversion function
convert_qe_to_cp2k(input_file, output_file)
