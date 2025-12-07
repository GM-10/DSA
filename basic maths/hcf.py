def main():
    n1=int(input("Enter a number:"))
    n2=int(input("Enter another number:"))
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    hcf=0
    for i in range(1,smaller+1):
        if((n1%i==0) and (n2%i==0)):
            hcf=i
    print("The HCF of",n1,"and",n2,"is",hcf)
    
if __name__ == "__main__":
    main()