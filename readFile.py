import numpy as np

f = open('dataset/data/imagedata.txt')
contents = f.read()
f.close()
#checkArray.reshape(1,220,220)
checkArray = np.fromstring(contents, dtype=int)
checkArray.reshape(3,220,220)
print(checkArray.shape)