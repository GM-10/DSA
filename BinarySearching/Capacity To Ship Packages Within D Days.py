def main():
    weights=list(map(int,input("Enter the weights of packages:").split()))
    days=int(input("Enter the number of days:"))
    high=sum(weights)
    low=max(weights)
    ans=0
    while low<=high:
        mid=(low+high)//2
        dailyweight=0
        day=1
        for weight in weights:
            if dailyweight+weight>mid:
                day+=1
                dailyweight=weight
            else:
                dailyweight+=weight
        if day<=days:
            high=mid-1
            ans=mid
        else:
            low=mid+1
    print(ans)

if __name__ == "__main__":
    main()