def main():
    size=int(input("Enter the size of array:"))
    arr=[]
    for i in range(size):
        ele=int(input("Enter element:"))
        arr.append(ele)
    reverse_arr=arr[::-1]
    return reverse_arr

if __name__ == "__main__":
    main()