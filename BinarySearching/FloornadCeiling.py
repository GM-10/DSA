def main():
    arr=list(map(int,input("Enter the sorted array:").split()))
    print(arr)
    x=int(input("Enter the element whose floor and ceiling is required to find: "))

    floor=-1
    low=0
    high=len(arr)-1
    ceiling=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            floor=arr[mid]
            low=mid+1
        else:
            high=mid-1
    print("Floor is ",floor)

    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ceiling=arr[mid]
            high=mid-1
        else:
            low=mid+1
    print("Ceiling is ",ceiling)
    print("The number if occurencs is :", ceiling-floor+1)

if __name__ == "__main__":
    main()