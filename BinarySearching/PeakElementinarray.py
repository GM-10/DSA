def main():
    arr=list(map(int,input("Enter the sorted rotated array:").split()))
    print(arr)
    if len(arr)==1:
        print(arr[0])
        return
    if arr[len(arr)-2]!=arr[len(arr)-1]:
        print(arr[len(arr)-1])
        return
    
    low=0
    high=len(arr)-1
    minvalue=float('inf')
    while low<=high:
        mid=(low+high)//2
        minvalue=min(minvalue,arr[mid])
        if arr[mid]!=arr[mid+1] & arr[mid-1]!=arr[mid]:
            print(arr[mid])
            return
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Move to the right half
            low = mid + 1
        else:
                # Move to the left half
            high = mid - 1
    return 


if __name__ == "__main__":
    main()