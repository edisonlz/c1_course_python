#coding=utf-8
问:合并两个有序序列,合并后依然有序

a1 = [1,3,5,7,9]
b2 = [2,4,6,8,10,12,14]

def merge_list(a,b,temp=[]):
    if len(a) == 0 or len(b) == 0:
        temp.extend(a)
        temp.extend(b)

        return temp
    else:

        if a[0]<b[0]:
            temp.append(a[0])
            del a[0]
        else:
            temp.append(b[0])
            del b[0]

        return merge_list(a,b,temp)

c = merge_list(a1,b2,[])



        





























