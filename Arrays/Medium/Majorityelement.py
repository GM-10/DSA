#this follows the moore voting algorithm
def main():
    arr=list(map(int,input("Enter the arrau").split()))
    print(arr)
    ele=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]==ele and count>=0:
            count+=1
        elif arr[i]!=ele and count>=0:
            count-=1
        if count==0:
            ele=arr[i]
            count=1
    print("Majority element is:",ele)

if __name__ == "__main__":
    main()