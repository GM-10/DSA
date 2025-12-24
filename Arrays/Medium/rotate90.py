def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(matrix)
    for i in range(n):
        for j in range(i,m):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix=[matrix[i][::-1] for i in range(n)]
    print(matrix)

if __name__ == "__main__":
    main()