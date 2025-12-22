def main():
    nums=list(map(int,input("Enter the array:").split()))
    print(nums)
    max_sum=0
    curr_sum=0
    for i in range(len(nums)):
        if curr_sum==0:
            start=i

        curr_sum+=nums[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
            end=i
        elif curr_sum<0:
            curr_sum=0
    if curr_sum==0:
        start=end=None
        max_sum=0

    print("Maximum sum is:",max_sum)
    print("Subarray indices are:",start,"to",end)

if __name__ == "__main__":
    main()