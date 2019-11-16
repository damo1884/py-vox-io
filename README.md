# Vox Slicer

## Note:
Input vox file must be square and a multiple of the output slice size

## Make sure to add the root of this project to the PYTHON_PATH

`export PYTHONPATH="<path to where you saved this project>/py-vox-io/"`

## Usage: 
`python slicer.js <input filename> <output folder> <slice size>`

## Example:
`python slicer.py ./models/64x64x64.vox ./out 32`

 - Sliced Vox files will be created in the ./out folder.
