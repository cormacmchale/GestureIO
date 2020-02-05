import numpy as np
#f = open('dataset/data/imagedata.txt')
#contents = f.read()
#f.close()
#checkArray.reshape(1,220,220)
checkArray = np.loadtxt('dataset/data/data.csv',delimiter=',')
#checkArray.reshape(2,220,220)
print(checkArray.shape)
print(checkArray.size)