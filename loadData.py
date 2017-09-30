import numpy as np

def loadSimpData():
    datMat = np.matrix([[ 1. , 2.1],
                     [ 2. , 1.1],
                     [ 1.3, 1. ],
                     [ 1. , 1. ],
                     [ 2. , 1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = []
    labelMat = []
    fr = open(fileName)
for line in fr.readlines():
lineArr =[]
curLine = line.strip().split('\t')
for i in range(numFeat-1):
lineArr.append(float(curLine[i]))
dataMat.append(lineArr)
labelMat.append(float(curLine[-1]))
return dataMat,labelMat

datMat,classLabels = loadSimpData()

