#!/bin/bash

for i in {00001..00111};
do
  cat header.in supercell/supercell-$i.in > input/Si-$i.in;
  mpirun -np 4 pw.x -inp input/Si-$i.in > output/Si-$i.out;
done
