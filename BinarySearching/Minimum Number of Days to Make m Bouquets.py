def main():
    bloomDay=list(map(int,input("Enter the bloom days of flowers:").split()))
    print(bloomDay)
    m=int(input("Enter the number of bouquets needed:"))
    k=int(input("Enter the number of flowers per bouquet:"))
    n=len(bloomDay)
    if m*k>n:
        return -1
    low=min(bloomDay)
    high=max(bloomDay)
    finalAns=-1
    while low<=high:
        mid=(low+high)//2
        bouquets=0
        flowers=0
        for day in bloomDay:
            if day <= mid:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        if bouquets >= m:
            finalAns = mid
            high = mid - 1
        else:
            low = mid + 1
    print(finalAns)

if __name__ == "__main__":
    main()