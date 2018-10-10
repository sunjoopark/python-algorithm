FALSE = 0
TRUE = 1
INT_MAX = 10000
m = [
[ 1, 5, 3 ],
[ 2, 5, 7 ],
[ 5, 3, 5 ]
]
col_check = [ FALSE, FALSE, FALSE ]
min_sol = INT_MAX
def f(row, score):
    global min_sol
    if row == 3:
        if score < min_sol :
            min_sol = score
        return min_sol
    for i in range(3):
        if col_check[i] == FALSE:
            col_check[i] = TRUE
            f(row + 1, score + m[row][i])
            col_check[i] = FALSE
    return min_sol
if __name__ == "__main__":
    print("min_sol : %d"%(f(0,0)))