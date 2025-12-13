def getSecondOrderElements(n,a):
    # Write your code here.
    largest=float('-inf')
    smallest=float('inf')
    secondsmallest=float('inf')
    secondlargest=float('-inf')
    for i in range(len(a)):
        if a[i]<smallest:
            secondsmallest=smallest
            smallest=a[i]
        elif (smallest<a[i]<secondsmallest):
            secondsmallest=a[i]
        if a[i]>largest:
            secondlargest=largest
            largest=a[i]
        elif largest>a[i]>secondlargest:
            secondlargest=a[i]
    return [secondlargest,secondsmallest]
    pass
def main():
    n=int(input())
    a=list(map(int,input().split()))
    result=getSecondOrderElements(n,a)
    print(result)
if __name__ == "__main__":
    main()