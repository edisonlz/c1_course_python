分治法 快速排序
将一个问题划分成若干个子问题，递归解决
O(nLogn)

pivot = 6
[6 ,10, 13, 5, 8, 3, 2]
 i  j        

pivot = 6
[6 ,5, 3, 2, 8, 13, 10]
          i          j        

[2 ,5, 3] 6 [ 8, 13, 10]
          i          j       


def partition(datas,low,high):
    pivot = datas[low]
    i = low

    for j in range(low+1,high+1):
        if datas[j]<pivot:
            i+=1
            datas[i], datas[j] = datas[j] , datas[i]

    datas[i],datas[low] = datas[low] , datas[i]
    return i


def quick_sort(datas,low,high):
    if low<high:
        print("low:%s,high:%s" % (low,high))
        pivot = partition(datas,low,high)
        print(datas)
        quick_sort(datas,low,pivot - 1)
        quick_sort(datas,pivot+1,high)

datas = [6 ,10, 13, 5, 8, 3, 2]
quick_sort(datas,0,len(datas) -1 )
































# def partition(datas,low,high):
#     pivot = datas[low]
#     i = low
#     for j in range(low+1 , high+1):
#         if datas[j]<pivot:
#             i+=1
#             datas[i], datas[j] = datas[j], datas[i]
    
#     datas[low], datas[i] = datas[i], datas[low]
#     return i



# def quick_sort(datas, low, high):
#     if low<high:
#         print("%s:%s" % (low,high))
#         pivot = partition(datas,low,high)
#         print(datas)
#         quick_sort(datas ,low ,pivot-1)
#         quick_sort(datas, pivot+1 ,high)


# datas = [6 ,10, 13, 5, 8, 3, 2]
# quick_sort(datas, 0 , len(datas)-1)

print(datas)

