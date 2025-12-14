def main():
    arr=list(map(int,input("Enter the array that contains only 0 and 1:").split()))
    print(arr)
    count=0
    maxcount=0
    for i in arr:
        if i==1:
            count+=1
            if maxcount<count:
                maxcount=count
        else:
            count=0
    print("The maximum consecutive 1 is:",maxcount)   

if __name__ == "__main__":
    main()