# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_zeros_ones(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1 
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    arr= list(map(int, input().split()))
    sort_zeros_ones(arr)
    results.append(" ".join(map(str, arr)))
for result in results:
    print(result)
