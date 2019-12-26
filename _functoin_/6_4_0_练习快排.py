练习&作业 1.快速排序
快速排序使用分治法策略来把一个序列分为较小和较大的2个子序列，然后递归地排序两个子序列。

1）快速排序是分治法
2) 利用递归简化实现
3）不额外占用内存空间
4）时间复杂度O(nlog2n)

def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high]     
    for j in range(low , high): 
        # 当前元素小于或等于 pivot 
        if arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
for i in range(n): 
    print ("%d" %arr[i])
