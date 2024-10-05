#!/bin/bash

# Loop through the desired range of indices
for i in {00001..00003}; do  # Adjust the upper limit as needed
    # Create the directory disp-$i
    dir_name="disp-$i"
    mkdir -p "$dir_name"

    # Copy coord$i.in to the disp-$i directory
    cp "/home/cyk/Phono3py/convert/coord$i.in" "$dir_name/"

    # Rename coord$i.in to coord.in within the disp-$i directory
    mv "$dir_name/coord$i.in" "$dir_name/coord.in"

    # Change to the disp-$i directory
    cd "$dir_name" 

    # Download the supercell.inp file
    wget https://raw.githubusercontent.com/chanyongkeat/researchshg/refs/heads/main/phono3py/qe2cp2k/supercell.inp

    # Change back to the original directory (optional)
    cd ..
done
