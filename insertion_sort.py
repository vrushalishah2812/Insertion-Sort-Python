def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

a = int(input("Enter total number for a list : "))
l = []
for i in range(0,a) :
    temp = int(input("Enter {} number : ".format(i+1)))
    l.append(temp)
insertionSort(l)
print("Sorted list is : {}".format(l))