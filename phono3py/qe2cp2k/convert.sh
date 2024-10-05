#!/bin/bash

# Define the base name for the input and output files
input_base="supercell-"
output_base="coord"

# Loop through the range 1 to 111
for i in {00001..00003}; do
    # Generate input and output file names
    qe_file="${input_base}${i}.in"
    cp2k_file="${output_base}${i}.in"

    # Call the Python script with the generated file names
    python convert.py "$qe_file" "$cp2k_file"
done
