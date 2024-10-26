import os

# Path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through the range for multiple files (001 to 010)
for i in range(1, 11):
    # Define input and output filenames
    poscar_filename = f"Raman-POSCAR.0004.{i:03}.vasp"
    qe_input_filename = f"coord.0004.{i:03}.in"
    
    # Full paths for input and output files
    poscar_filepath = os.path.join(current_dir, poscar_filename)
    qe_input_filepath = os.path.join(current_dir, qe_input_filename)

    # Check if the POSCAR file exists
    if not os.path.isfile(poscar_filepath):
        print(f"{poscar_filename} does not exist, skipping.")
        continue

    # Read the POSCAR file
    with open(poscar_filepath, 'r') as poscar_file:
        lines = poscar_file.readlines()

    # Extract the scaling factor and lattice vectors
    scaling_factor = float(lines[1].strip())
    lattice_vectors = [
        [float(x) * scaling_factor for x in lines[2].split()],
        [float(x) * scaling_factor for x in lines[3].split()],
        [float(x) * scaling_factor for x in lines[4].split()]
    ]

    # Extract atomic types and counts
    atomic_types = lines[5].split()
    atomic_counts = list(map(int, lines[6].split()))

    # Extract atomic positions
    positions = lines[8:]

    # Prepare Quantum Espresso input content
    qe_content = []

    # Format CELL_PARAMETERS section
    qe_content.append("CELL_PARAMETERS angstrom")
    for vector in lattice_vectors:
        qe_content.append("   " + "    ".join(f"{v:.10f}" for v in vector))

    # Format ATOMIC_POSITIONS section
    qe_content.append("\nATOMIC_POSITIONS crystal")
    for atom, count in zip(atomic_types, atomic_counts):
        for _ in range(count):
            position_line = positions.pop(0).strip().split()
            qe_content.append(f" {atom}   " + "    ".join(position_line))

    # Write to Quantum Espresso input file
    with open(qe_input_filepath, 'w') as qe_file:
        qe_file.write("\n".join(qe_content))

    print(f"Quantum Espresso input file saved as {qe_input_filename}")
