def main():
    arr=list(map(int,input("Enter the array elements:").split()))
    print(arr)
    pos=0 #Position of the next non zero
    for i in range(len(arr)-1):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    print("The array after moving zeros to end is")
    print(arr)

if __name__ == "__main__":
    main()