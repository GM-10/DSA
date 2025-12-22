'''
Brute force will be to check for each elemment summing them, n^2 time complexity
Better approach is to use hashmap to store the count of prefix sums, and for each element check if (current_sum - k) exists in the hashmap
This will take O(n) time and O(n) space
Best approach is:
2 pointer approach, we keep the array sorted
'''

def main():
    arr=list(map(int,input("Enter the array:").split()))
    print(arr)
    k=int(input("Enter the sum that you need from the subarray:"))
    left =0
    right = len(arr)-1
    while left<right:
        if arr[left]+arr[right]==k:
            print("Found at",left,"and",right)
            return True
        elif arr[left]+arr[right]<k:
            left+=1
        else:
            right-=1
    print("Not Found")
    return False

if __name__ == "__main__":
    main()