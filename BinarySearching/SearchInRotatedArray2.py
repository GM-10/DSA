def main():
    arr=list(map(int,input("Enter the sorted rotated array:").split()))
    print(arr)
    target=int(input("Enter the element to be searched: "))
    low=0
    high=len(arr)-1
    ans=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=1
        if arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    if ans==1:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()