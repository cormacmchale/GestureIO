csvfile = open('dataset/data/imagedata.csv', 'r').readlines()

filename = 'imagedata.csv'
for i in range(len(csvfile)):
     if i > 220 == 0:
         open(filename, 'w+').writelines(csvfile[i:i+1000])
         filename = 'new.csv'