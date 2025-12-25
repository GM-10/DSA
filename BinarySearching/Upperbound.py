def main():
    arr=list(map(int,input("Enter the sorted array:").split()))
    print(arr)
    x=int(input("Enter the element whose upper bound is required to find: "))

    ans=len(arr)
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print("Upper bound is ",ans)


if __name__ == "__main__":
    main()