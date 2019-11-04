# Hour glass sum https://www.hackerrank.com/challenges/2d-array/problem
# Input:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
if __name__ == '__main__':
    arr = [list(map(int, input().rstrip().split())) for _ in range(6)]
    results = []
    for i, row in enumerate(arr[:4]):
        for j, value in enumerate(row[:4]):
            results.append(sum([value, row[j + 1], row[j + 2], arr[i + 1][j + 1], arr[i + 2][j], arr[i + 2][j + 1],
                                arr[i + 2][j + 2]]))

    print(max(results))
