"""
算法步骤
1.比较相邻的元素，如果第一个比第二个大，就交换他们连个
2.对每一相邻的元素做同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
3.针对所有元素做同样的步骤，除了最后一个
4.持续每次对越来越少的元素重复上面的步骤，知道没有任何一对需要比较
https://github.com/hustcc/JS-Sorting-Algorithm
"""

def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    print(bubbleSort([1,6,7,3,24,5,78]))