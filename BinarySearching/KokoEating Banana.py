def main():
    piles=list(map(int,input("Enter the sorted rotated array:").split()))
    print(piles)
    h=int(input("Enter the hour limit:"))
    low=1
    high=max(piles)
    ans=high
    while low<=high:
        mid=(low+high)//2
        total=0
        for bananas in piles:
            total+=(bananas+mid-1)//mid

        if total<=h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print(ans)

if __name__ == "__main__":
    main()