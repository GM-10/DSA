def main():
    str=input("Enter a string:")
    reversedstr=str[::-1]
    if str== reversedstr:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
if __name__ == "__main__":
    main()