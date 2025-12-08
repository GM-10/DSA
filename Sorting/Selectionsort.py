#Bring minimum to front and then do the loop for next remaining elements
def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    print("Sorted array is: ")
    print(arr)
if __name__ == "__main__":
    main()