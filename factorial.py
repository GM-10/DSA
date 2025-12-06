def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Enter the n:")
    n=int(input())
    ans= factorial(n)
    print("Factorial is:", ans)

if __name__ == "__main__":
    main()