from numpy import *


def file2matrix(filename):
    fr = open(filename,'r')
    nunberLines = len(fr.readlines())
    returnMat = zeros((nunberLines,3))
    classLabelVector=[]
    fr = open(filename,'r')
    index=0
    for line in fr.readlines():
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index+=1
    return returnMat,classLabelVector


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    # print(diffMat)
    sqDiffMat = diffMat**2
    # print(sqDiffMat)
    sqDistance = sqDiffMat.sum(axis=1)
    # print(sqDistance)
    distance = sqDistance**0.5
    sortedDistIndicies = distance.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=lambda x:x[1],reverse=True)
    return sortedClassCount[0][0]

def autuNorm(dataSet):
    # 标准化处理
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals -minVals
    normDataSet = zeros(dataSet.shape)
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals


def datingClassTest():
    hoRatio = 0.1
    datingDataMat,datingLabels = file2matrix('G:/AiLearning-dev/data/2.KNN/datingTestSet2.txt')
    normMat,ranges,minVals = autuNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    print('numTestVecs=',numTestVecs)
    errorsCount = 0
    for i in range(numTestVecs):
        classresult  = classify0(normMat[i],normMat[numTestVecs:m],datingLabels,3)
        print('the class result is %d,the real result is %d'%(classresult,datingLabels[i]))
        if classresult != datingLabels[i]:
            errorsCount+=1
    print('the error tate is %f'%(errorsCount/numTestVecs))
    print(errorsCount)

def main():
    datingClassTest()


if __name__ == '__main__':
    main()