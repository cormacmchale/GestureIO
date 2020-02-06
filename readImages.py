import numpy as np
#import pandas as pd
#f = open('dataset/data/imagedata.txt')
#contents = f.read()
#f.close()
checkArray = np.loadtxt('dataset/data/imagedata.npy')
checkArray = checkArray.reshape(600, 48400)
print(checkArray.shape)
print(checkArray.size)