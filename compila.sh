#!/bin/bash
export PATH=$PATH:~/omnetpp-4.6/bin
export LD_LIBRARY_PATH=~/omnetpp-4.6/lib
export LD_LIBRARY_PATH=~/usr/local/lib
make clean
./makemake
make
