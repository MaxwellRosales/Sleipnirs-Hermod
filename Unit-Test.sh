#! /bin/bash

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

# Runs pytest to unit test code in directory
echo
echo "############ Pytesting Code ##############"
echo
cd ./Vehicle-Python/Pytests
pytest