def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    largest=arr[0]
    secondlargest=-1
    for i in range(len(arr)):
        if arr[i]>largest:
            secondlargest=largest
            largest=arr[i]
        elif arr[i]>secondlargest and arr[i]!=largest:
            secondlargest=arr[i]
    print(secondlargest)

if __name__ == "__main__":
    main()