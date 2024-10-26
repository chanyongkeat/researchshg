import os

# Path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through the extracted dielectric files from 001 to 010
for i in range(1, 11):
    # Define input and output filenames
    dielectric_filename = f"Si-dielectric.0004.{i:03}.dat"
    outcar_filename = f"OUTCAR.0004.{i:03}"
    
    # Full paths for input and output files
    dielectric_filepath = os.path.join(current_dir, dielectric_filename)
    outcar_filepath = os.path.join(current_dir, outcar_filename)
    
    # Check if the dielectric file exists
    if not os.path.isfile(dielectric_filepath):
        print(f"{dielectric_filename} does not exist, skipping.")
        continue

    # Read the dielectric matrix data
    with open(dielectric_filepath, 'r') as dielectric_file:
        matrix_lines = dielectric_file.readlines()
    
    # Format the matrix into VASP-style output
    vasp_output = []
    vasp_output.append("   POMASS =   28.085; ZVAL   =    4.000    mass and valenz")
    vasp_output.append("   NIONS =      2")
    vasp_output.append("   ions per type = 2")
    vasp_output.append("")
    vasp_output.append(" MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT)")
    vasp_output.append(" ------------------------------------------------------")

    # Add the dielectric matrix, formatted as in VASP output
    for line in matrix_lines:
        vasp_output.append(f"           {line.strip()}")

    vasp_output.append(" ------------------------------------------------------")
    
    # Write the VASP-formatted dielectric tensor to the output file
    with open(outcar_filepath, 'w') as outcar_file:
        outcar_file.write("\n".join(vasp_output))
    
    print(f"VASP-style dielectric matrix saved to {outcar_filename}")
