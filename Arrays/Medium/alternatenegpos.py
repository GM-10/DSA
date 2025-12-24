def main():
    arr=list(map(int,input("Enter the elements of the array seperated by space:").split()))
    print(arr)
    newarr=[0]*len(arr)
    pos=0
    neg=1
    for i in range(len(arr)):
        if arr[i]<0:
            newarr[neg]=arr[i]
            neg+=2
        else:
            newarr[pos]=arr[i]
            pos+=2
    print(newarr)

if __name__ == "__main__":
    main()