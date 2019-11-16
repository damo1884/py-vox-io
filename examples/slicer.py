import sys
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter
from pyvox.models import Vox
from skimage.util.shape import view_as_blocks
import math  

m1 = VoxParser('./models/64x64x64.vox').parse()
print('Vox Slicer')
newSize = 32

data = m1.to_dense()
originalSize = len(data)
chunks = view_as_blocks(data, block_shape=(newSize, newSize, newSize))
outputCount = math.ceil((originalSize/newSize)*(originalSize/newSize)*(originalSize/newSize))
count = int(originalSize/newSize)

print('Input Size: ', originalSize)
print('Output Size: ', newSize)
print('Creating ', outputCount, ' Vox Files')

for z in range(0,count):
	for y in range(0,count):
		for x in range(0,count):
			print('chunk: ', x, y, z)
			chunk = chunks[x][y][z]
			vox = Vox.from_dense(chunk)
			filename = './out/'+str(x)+'-'+str(y)+'-'+str(z)+'.vox'
			VoxWriter(filename, vox).write()
			print('Created:', filename)
print('done')
