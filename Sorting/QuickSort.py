#Pick a pivot element from the array place it to its correct position in the array.
#Smaller on the left and larger on the right.
def partition(arr,low,high):
    pivot=low
    i=low+1
    j=high
    while(i<=j):
        while(i<=high and arr[i]<=arr[pivot]):
            i+=1
        while(arr[j]>arr[pivot] and j>=low):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[pivot],arr[j]=arr[j],arr[pivot]
    return j
    
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def main():
    arr=list(map(int,input("Enter the array elements with spaces:").split()))
    print (arr)
    low=0
    high=len(arr)-1
    quicksort(arr,low,high)

    print("Sorted array is:")
    print(arr)

if __name__ == "__main__":
    main()