import sys
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter
from pyvox.models import Vox
from skimage.util.shape import view_as_blocks
import math  

if len(sys.argv) < 4:
	print('Error: You must pass the input filename, output folder & slice size')
	print('Usage: python slicer.js <input filename> <output folder> <slice size>');
	print('eg. python slicer.js input.vox output.vox 32');
else:
	print('Vox Slicer Starting...')
	inputFile = sys.argv[1]
	outputPath = sys.argv[2]
	sliceSize = int(sys.argv[3])
	print('Input File: ', inputFile)
	print('Output Path: ', outputPath)
	print('Slice Size: ', sliceSize)
	m1 = VoxParser(inputFile).parse()
	
	data = m1.to_dense()
	originalSize = len(data)

	print('Input Vox Size: ', originalSize)
	print('Output Vox Slice Size: ', sliceSize)

	if originalSize % sliceSize != 0:
		print('Error: Input Vox size must be a multiple of Output Slice size')
	else:
		chunks = view_as_blocks(data, block_shape=(sliceSize, sliceSize, sliceSize))
		outputCount = math.ceil((originalSize/sliceSize)*(originalSize/sliceSize)*(originalSize/sliceSize))
		count = int(originalSize/sliceSize)

		
		print('Creating ', outputCount, ' Vox Files')

		for z in range(0,count):
			for y in range(0,count):
				for x in range(0,count):
					print('chunk: ', x, y, z)
					chunk = chunks[x][y][z]
					vox = Vox.from_dense(chunk)
					filename = outputPath + '/'+str(x)+'-'+str(y)+'-'+str(z)+'.vox'
					VoxWriter(filename, vox).write()
					print('Created:', filename)
		print('done')
