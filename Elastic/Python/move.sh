#!/bin/bash

# Loop through files Dst01_01.out to Dst01_05.out
for i in {01..05}
do
    # Define the file and corresponding folder name
    file="Dst01_${i}.out"
    folder="Dst01_${i}"

    # Move the file into the corresponding folder
    if [ -f "$file" ]; then
        mv "$file" "$folder/"
        echo "Moved $file to $folder/"
    else
        echo "$file does not exist!"
    fi
done
