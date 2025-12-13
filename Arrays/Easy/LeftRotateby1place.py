def main():
    arr=list(map(int,input("Enter the array elements:").split()))
    print(arr)
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    print("The array after 1 left rotation is:")
    print(arr)

if __name__ == "__main__":
    main()