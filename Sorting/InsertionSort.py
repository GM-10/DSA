#takes and element and insert it at right place in sorted array
def main():
        arr=list(map(int,input("Enter the array elements with spaces:").split()))
        print (arr)
        for i in range(len(arr)):
              for j in range(i,0,-1):
                    if arr[j]<arr[j-1]:
                          arr[j],arr[j-1]=arr[j-1],arr[j]
                    else:
                          break
        print("Sorted array is:")
        print(arr) 

if __name__ == "__main__":
    main()