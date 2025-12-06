def recursion(n,sum):
    sum=sum+n
    if n <= 0:
        print(sum)
        return    
    recursion(n-1,sum)
    

def main():
    n = int(input("Enter the n: "))
    recursion(n,0)

if __name__ == "__main__":
    main()
