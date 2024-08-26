def has_pair_with_difference(arr, N, K):
    seen = set()
    for num in arr:
        if (num - K) in seen or (num + K) in seen:
            return True 
        seen.add(num)
    return False 
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if has_pair_with_difference(arr, N, K):
        print("true")
    else:
        print("false")
