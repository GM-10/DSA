def main():
    arr=list(map(int,input("Enter the sorted rotated array:").split()))
    print(arr)
    
    low=0
    high=len(arr)-1
    minvalue=float('inf')
    while low<=high:
        mid=(low+high)//2
        minvalue=min(minvalue,arr[mid])
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid-1
    print("Minimum element in the sorted rotated array is :",minvalue)


if __name__ == "__main__":
    main()