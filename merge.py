# 15 BODLOGO

# task1
# def merge(left,right):
#     hariu=[]
#     i=0
#     j=0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             hariu.append(left[i])
#             i+=1
#         else:
#             hariu.append(right[j])
#             j+=1
#     hariu+=left[i:]
#     hariu+=right[j:]
#     return hariu
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     dund=len(arr)//2
#     zuun=merge_sort(arr[:dund])
#     baruun=merge_sort(arr[dund:])
#     return merge(zuun,baruun)
# too=[38,27,43,3,9,82,10]
# print(merge_sort(too))

# task2
def merge(left,right):
    hariu=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            hariu.append(left[i])
            i+=1
        else:
            hariu.append(right[j])
            j+=1
    hariu+=left[i:]
    hariu+=right[j:]
    return hariu
def merge_sort_desc(arr):
    if len(arr)<=1:
        return arr
    dund=len(arr)//2
    zuun=merge_sort_desc(arr[:dund])
    baruun=merge_sort_desc(arr[dund:])
    return merge(zuun,baruun)
too=[38,27,43,3,9,82,10]
print(merge_sort_desc(too))