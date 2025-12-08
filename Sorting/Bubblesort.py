#Pushes the largest to last

def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("Sorted array is:")
    print(arr)

if __name__ == "__main__":
    main()