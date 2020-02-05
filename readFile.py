import numpy as np
import pandas as pd
# f = open('dataset/data/imagedata.txt')
# contents = f.read()
# f.close()

checkArray = np.loadtxt('dataset/data/imagedata.csv', delimiter=',')
checkArray.reshape(2, 220, 220)
# checkArray.reshape(2, 220, 220)

data = pd.read_csv('dataset/data/imagedata.csv') 
totalInstances = len(data) + 1

for i in data:
    if len(data) + 1 > 220:
        print("hello friend")

print(checkArray.shape)
print(checkArray.size)
print(totalInstances)