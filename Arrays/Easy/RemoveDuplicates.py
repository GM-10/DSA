def main():
    arr=list(map(int,input().split()))
    print(arr)
    unqarr=list(set(arr))
    print("THe array after removing duplicates is:")
    print(unqarr)

if __name__ == "__main__":
    main()