import numpy as np
#import pandas as pd
#f = open('dataset/data/imagedata.txt')
#contents = f.read()
#f.close()
checkArray = np.loadtxt('dataset/data/imagedata.csv')
checkArray = checkArray.reshape(199, 220, 220)
print(checkArray.shape)
print(checkArray.size)