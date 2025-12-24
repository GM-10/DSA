def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(matrix)
    col_0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col_0=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col_0==0:
        for i in range(n):
            matrix[i][0]=0
    print(matrix)
if __name__ == "__main__":
    main()