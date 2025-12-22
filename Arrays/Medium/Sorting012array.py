#Dutch national flag algorithm to sort an array of 0s, 1s and 2s in a single traversal or can be called as 3 pointer appraoch
def main():
    arr=list(map(int,input("Enter the array:").split()))
    print(arr)
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print("Sorted array is:",arr)

    

if __name__ == "__main__":
    main()