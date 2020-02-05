import numpy as np
#import pandas as pd
#f = open('dataset/data/imagedata.txt')
#contents = f.read()
#f.close()
checkArray = np.loadtxt('dataset/data/imagedata.csv', delimiter=',')
checkArray = checkArray.reshape(2, 220, 220)

np.savetxt("newImage.csv", checkArray[0], delimiter=',', fmt='%s')