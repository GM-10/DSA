def main():
    arr=list(map(int,input("Enter the array elements:").split()))
    print(arr)
    d=int(input("Enter the number of places you wnat the array to be rotated by:"))
    n=len(arr)
    d=d%n
    arr[0:d]=arr[0:d][::-1]
    arr[d:n]=arr[d:n][::-1]
    arr=arr[::-1]
    
    print("The array after",d," left rotation is:")
    print(arr)

if __name__ == "__main__":
    main()