def f(a, b):
    if a == b:
        return 0
    if b > a:
        return f(a, b // 2) + 1
    if a > b:
        return f(a // 2, b) + 1

if __name__ == "__main__":
    a = int(input("첫 번째 노드 : "))
    b = int(input("두 번째 노드 : "))
    print("%d와 %d의 거리 : %d"%(a,b,f(a,b)))