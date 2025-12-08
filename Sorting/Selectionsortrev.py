def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    for i in range(len(arr)):
        max_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[max_idx]:
                max_idx=j
        arr[i],arr[max_idx]=arr[max_idx],arr[i]
    print("Sorted array is: ")
    print(arr)
if __name__ == "__main__":
    main()