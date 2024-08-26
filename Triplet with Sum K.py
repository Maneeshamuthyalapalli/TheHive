def find_triplet_sum(arr, N, K):
    arr.sort()
    for i in range(N - 2):
        left = i + 1
        right = N - 1
        while left < right:
            current_sum  = arr[i] + arr[left] + arr[right]
            if current_sum == K:
                return True 
            elif current_sum < K:
                left += 1 
            else:
                right -= 1 
    return False 
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if find_triplet_sum(arr, N, K):
        print("true")
    else:
        print("false")
