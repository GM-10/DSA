def recursion(n):
    print(n)
    if n <= 0:
        return
    
    recursion(n-1)
    

def main():
    n = int(input("Enter the n: "))
    recursion(n)

if __name__ == "__main__":
    main()
