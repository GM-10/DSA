#2 pointer approach

def main():
    arr=list(map(int,input("Enter the array that contains only 0 and 1:").split()))
    print(arr)
    k=int(input("Enter the sum that you need from the subarray:"))
    maxlen=0
    left=0
    right=0
    sum=arr[0]
    while right<len(arr):
        while left<=right and sum>k:
            sum-=arr[left]
            left+=1
        if sum==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<len(arr):
            sum+=arr[right]

    print("The longest subarray is:",maxlen)   

if __name__ == "__main__":
    main()