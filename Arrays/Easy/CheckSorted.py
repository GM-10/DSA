def main():
    arr=list(map(int,input("Enter the array:").split()))
    print(arr)
    flag=1
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            flag=0
            print("THe array is not sorted:")
            break
    if(flag==1):
        print("The array is sorted")


if __name__ == "__main__":
    main()