# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_missing_number(arr, n):
    total_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum 
T = int(input())
results = [] 
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    missing_number = find_missing_number(arr, N)
    results.append(missing_number)
for result in results:
    print(result)
