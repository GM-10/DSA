#divide and merge
def merge(arr,left,mid,right):
    left_arr=arr[left:mid]
    right_arr=arr[mid:right]
    i=0
    j=0
    k=left
    while(i<len(left_arr) and j<len(right_arr)):
        if(left_arr[i]<right_arr[j]):
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
        k+=1        
    while(i<len(left_arr)):
        arr[k]=left_arr[i]
        i+=1
        k+=1        
    while(j<len(right_arr)):
        arr[k]=right_arr[j]
        j+=1
        k+=1
    return arr
def merge_sort(arr, left,right):
    if(left+1>=right):
        return
    mid=(left+right)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid,right)
    merge(arr,left,mid,right)
    return arr
def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print(arr)
    n=len(arr)
    arr=merge_sort(arr, 0,n)
    print("Sorted array is:")
    print(arr)


if __name__ == "__main__":
    main()