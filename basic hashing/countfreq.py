def main():
    n=int(input("Enter the size of the array: "))
    
    arr=input("Enter the elements of the array separated by space: ").split()
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print("Frequency of elements in the array is:",freq)

if __name__ == "__main__":
    main()