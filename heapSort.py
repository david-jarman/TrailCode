arr = []

def heapify(_arr):
    start=(len(_arr)//2) - 1 #dont heapify leaf nodes
    for i in range(start,-1,-1): #count backwards from the leaf nodes in the array
        maxHeapify(_arr,i)

def maxHeapify(_arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    heap_len = len(_arr)

    if left < heap_len and _arr[left] > _arr[largest]:
        largest = left

    if right < heap_len and _arr[right] > _arr[largest]:
        largest = right

    if largest != i:
        swap(_arr, i, largest)
        maxHeapify(_arr, largest)
   
def swap(_arr, pos1, pos2):
    _arr[pos1], _arr[pos2] = _arr[pos2], _arr[pos1]

def siftDown(_arr, start, end):
    root = start
    while 2*root+1 < end:
        left=2*root+1
        swapo = root
        if _arr[left]>_arr[root]:
            swapo=left
        if left+1<end and _arr[left+1]>_arr[swapo]:
            swapo=left+1

        if root == swapo:
            return

        swap(_arr, root, swapo)
        root = swapo

def heapSort(_arr):
    heapify(_arr)
    for i in range(0,len(_arr)):
        end = len(_arr) - 1 - i
        swap(_arr, 0, end)
        siftDown(_arr, 0, end)

arr = [15,2,16,3,1,4,5,14,6,7,17,8,11,18,12,13,9,10]
heapSort(arr)
print arr
