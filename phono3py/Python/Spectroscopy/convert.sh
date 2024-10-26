#!/bin/bash

for i in {001..007};
do
  cat header.in coord.0004.$i.in > Si-ph.0004.$i.in;
done
