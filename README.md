# Vox Slicer

## Note:
Input vox file must be a perfect cube and the size must be a multiple of the output slice size.

## Install Python 3

See: https://realpython.com/installing-python/

## Make sure to add the root of this project to the PYTHON_PATH

`export PYTHONPATH="<path to where you saved this project>/py-vox-io/"`

To verify PYTHONPATH is set run

`echo $PYTHONPATH`

## Check Python Version: 

Check if python is running python3

`python --version`

This should print something like 

`Python 3.7.4`

## Prerequisites 

`pip install scikit-image`

If using pip3 alias

`pip3 install scikit-image`

## Usage: 

`python slicer.js <input filename> <output folder> <slice size>`

or if using python3 alias

`python3 slicer.js <input filename> <output folder> <slice size>`

## Example:

From the examples folder run (`cd examples` to get into the folder)

`python slicer.py ./models/64x64x64.vox ./out 32`

 - Sliced Vox files will be created in the ./out folder.
 
 
