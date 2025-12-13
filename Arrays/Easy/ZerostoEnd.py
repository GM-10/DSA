def main():
    arr=list(map(int,input("Enter the array elements:").split()))
    print(arr)
    for i in range(len(arr)-1):
        if arr[i]==0:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    print("The array after moving zeros to end is")
    print(arr)

if __name__ == "__main__":
    main()