import pandas as pd

arr = [3,1,2,4]
arr.sort()
arr

arr = [1,1,2,3]
arr.remove(1)
arr

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr1.remove(2)
arr1

arr2 = [2,1,4,3,9,6]



def relativeSortArray(arr1, arr2):
    arr3 = []
    for i in arr2: # short list
        for j in arr1: # long list
            if j == i:
                print("list found", "i=", i, "j=", j)
                arr3.append(j)
                arr1.remove(j)
                print("arr1=", arr1)
            else:
                print("list not found", "i=", i, "j=", j)
    arr3.extend(arr1)
    return arr3

relativeSortArray(arr1, arr2)
