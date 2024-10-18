#!/bin/bash

for i in $(seq -w 001 234);
do
  docker run --rm --shm-size=1g -v $PWD:/mnt -u $(id -u $USER):$(id -g $USER) cp2k/cp2k:2024.3_mpich_generic_psmp mpirun -n 90 -genv OMP_NUM_THREADS=2 cp2k -i NBBFC-supercell-$i.inp > output/NBBFC-supercell-$i.out;
done
