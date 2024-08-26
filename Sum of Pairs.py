def has_pair_with_sum(arr, N, K):
    seen_numbers = set()
    for num in arr:
        complement = K - num 
        if complement in seen_numbers:
            return True 
        seen_numbers.add(num)
    return False
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if has_pair_with_sum(arr, N, K):
        print("True")
    else:
        print("False")
