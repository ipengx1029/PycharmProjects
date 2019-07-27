
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,4],[1.1,4.5],[3,0],[4.7,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    # print(diffMat)
    sqDiffMat = diffMat**2
    # print(sqDiffMat)
    sqDistance = sqDiffMat.sum(axis=1)
    # print(sqDistance)
    distance = sqDistance**0.5
    print(distance)
    sortedDistIndicies = distance.argsort()
    print(sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=lambda x:x[1],reverse=True)
    return sortedClassCount[0][0]

def test1():
    group,labels = createDataSet()
    result=classify0([2.4,2],group,labels,3)
    print(result)

if __name__ == '__main__':
    test1()