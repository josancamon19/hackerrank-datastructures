if __name__ == '__main__':

    _, d = input().split()
    a = list(map(str, input().split()))

    # Option 1
    # print(' '.join(a[d:] + a[:d]))

    # Option 2
    for _ in range(int(d)):
        a.insert(len(a) - 1, a.pop(0))
    print(' '.join(a))
