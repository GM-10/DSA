def main():
    nums=list(map(int,input("Enter the array of numbers:").split()))
    threshold=int(input("Enter the threshold:"))
    low=1
    high=max(nums)
    ans=0
    while low<=high:
        currsum=0
        mid=(low+high)//2
        for num in nums:
            currsum+=(num+mid-1)//mid
        if currsum<=threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

if __name__ == "__main__":
    main()