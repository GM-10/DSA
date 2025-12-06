def main():
    n=int(input("Enter a non-negative integer: "))
    print("The number of digits in n is:")
    if n>0:
        return int(math.log10(n)//1) +1
    elif n==0:
        return 1
    else:
        return "Invalid input! Please enter a non-negative number."
if __name__ == "__main__":
    import math
    ans= main()
    print(ans)