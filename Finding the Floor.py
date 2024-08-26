import bisect
def find_floor(arr, x):
    idx = bisect.bisect_right(arr, x)
    if idx == 0:
        return -2147483648
    return arr[idx -1]
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
Q = int(input())
queries = [int(input()) for _ in range(Q)]
for x in queries:
    print(find_floor(arr, x))
