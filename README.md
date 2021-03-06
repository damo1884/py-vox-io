# Vox Slicer

## Chrome Extension

This is for recombining the sliced vox files and placing them into https://cryptovoxels.com

### Cryptovoxels Generator

https://chrome.google.com/webstore/detail/cryptovoxel-generator/kodjbgifejfaajgpjjddifagocboccab

## Note:
Input vox file must be a perfect cube and the size must be a multiple of the output slice size.

## Install Python 3

See: https://realpython.com/installing-python/

## Download the code to your machine

Use the Download as Zip option by clicking the Green "Clone or Download" button to the top right.

## Make sure to add the root of this project to the PYTHON_PATH

Copy the path where you saved the file to

### Windows

`SET PYTHONPATH="<path to where you saved this project>\py-vox-io\"`

To verify PYTHONPATH is set run

`echo %PYTHONPATH%`

### MacOS
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
 
 
