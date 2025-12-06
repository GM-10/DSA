def recursion(n):
    print("Grishma")
    n = n - 1
    if n < 0:
        return
    recursion(n)

def main():
    n = int(input("Enter the number of times you need to print the name: "))
    recursion(n)

if __name__ == "__main__":
    main()
