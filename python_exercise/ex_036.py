cnt = 0
checked = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
def solve(n, a, b, c):
    global cnt
    if a + b + c == n :
        if a <= b and b <= c and a + b > c and checked[a][b][c] == 0:
            cnt = cnt + 1
            checked[a][b][c] = 1
        return
    solve(n, a + 1, b, c)
    solve(n, a, b + 1, c)
    solve(n, a, b, c + 1)

if __name__ == "__main__":
    n = 10
    solve(n, 1, 1, 1)
    print("만들 수 있는 삼각형의 갯수 : %d"%(cnt))