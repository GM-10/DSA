def main():
    arr=list(map(int,input("Enter the array elements:").split()))
    print(arr)
    n=arr[len(arr)-1]
    expectedsum=n*(n+1)//2
    
    actualsum=sum(arr)
    
    missingnumber=expectedsum-actualsum
    print("The missing number is:",missingnumber)   

if __name__ == "__main__":
    main()