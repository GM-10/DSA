def main():
    arr1=list(map(int,input("Enter the array elements in sorted order:").split()))
    print("Array 1 is: ",arr1)
    arr2=list(map(int,input("Enter the second array elements in sorted order:").split()))
    print("Array 2 is: ",arr2)
    newarr=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            newarr.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            newarr.append(arr2[j])
            j+=1
        else:
            newarr.append(arr1[i])
            i+=1
            j+=1
    while(i<len(arr1)):
        newarr.append(arr1[i])
        i+=1
    while (j<len(arr2)):
        newarr.append(arr2[j])
        j+=1
        
    print("The union of arrays is")
    print(newarr)

if __name__ == "__main__":
    main()