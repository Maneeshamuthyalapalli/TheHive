def non_divisible_subset(N, K, arr):
    remainder_count = [0] * K 
    for num in arr:
        remainder_count[num % K] += 1 
    max_subset_size = min(remainder_count[0], 1)
    for i in range(1, (K // 2) + 1):
        if i !=  K - i:
            max_subset_size += max(remainder_count[i], remainder_count[K - i])
        else:
            max_subset_size += min(remainder_count[i], 1)
    return max_subset_size
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(non_divisible_subset(N, K, arr))
