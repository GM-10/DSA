def main():
    x=int(input("Enter the number to find the square root of:"))
    start=0
    end=x
    ans=0
    while start<=end:
        mid=(start+end)//2
        if mid*mid <= x:
            ans=mid     
            start=mid+1
        else:
            end=mid-1
    print(ans)

if __name__ == "__main__":
    main()