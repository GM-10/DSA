def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    maximum=arr[0]
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
    print(maximum)

if __name__ == "__main__":
    main()