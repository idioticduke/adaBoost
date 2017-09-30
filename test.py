import numpy as np
import train
import loadData as ld
import stumpGenerate as sg

datMat,classLabels = ld.loadSimpData()
classifierArray = train.adaBoostTrainDS(datMat,classLabels,30)

def adaClassify(datToClass,classifierArr):
    dataMatrix = np.mat(datToClass)
    m = np.shape(dataMatrix)[0]
    aggClassEst = np.mat(np.zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst = sg.stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha']*classEst
        print (aggClassEst)
    return np.sign(aggClassEst)

#print (adaClassify([0, 0], classifierArray))
print (adaClassify([[5, 5],[0,0]],classifierArray))