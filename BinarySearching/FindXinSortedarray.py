def main():
    arr=list(map(int,input("Enter the sorted array elements:").split()))
    print(arr)
    x=int(input("Enter the element to be searched: "))
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    while low<=high:
        if arr[mid]==x:
            print("Element found at ",mid)
            break
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1

        mid=(low+high)//2
    
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()