def main():
    n=int(input("Enter a non negative number:"))
    reverse=str(n)[::-1]
    reverse=int(reverse)
    print("The reverse of the number is:",reverse)

if __name__ == "__main__":
    main()