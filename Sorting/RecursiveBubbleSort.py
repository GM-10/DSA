#Pushes the largest to last
def bubble_sort(arr,n):
    if n==1:
        return
    swap=False
    for j in range(0,n-1,1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=True
    if not swap:
        return
    bubble_sort(arr,n-1)   
def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    bubble_sort(arr,len(arr))
    print("Sorted array is:")
    print(arr)

if __name__ == "__main__":
    main()