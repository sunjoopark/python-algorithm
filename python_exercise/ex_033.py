def f(end):
    if end < 'A' or end > 'Z':
        return -1
    c = ord('A')
    while c <= ord(end):
        print("%2c"%(c), end ="")
        c = c + 1
    print()
    next = ord(end) - 1
    return f(chr(next))

if __name__ == "__main__":
    f('Z')