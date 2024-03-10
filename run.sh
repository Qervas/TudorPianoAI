#!/bin/bash
root_dir=$(pwd)
mkdir -p build
cd build
cmake ..
make 
cd $root_dir
./build/TudorPianoAI