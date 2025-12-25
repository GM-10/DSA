def main():
    arr=list(map(int,input("Enter the sorted array:").split()))
    print(arr)
    x=int(input("Enter the element to find lower bound for: "))
    ans=len(arr)
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    
    print("Search Insert position is ",ans)

if __name__ == "__main__":
    main()