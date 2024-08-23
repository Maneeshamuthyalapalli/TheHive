# Enter your code here. Read input from STDIN. Print output to STDOUT
def bubble_sort(arr):
    n = len(arr)
    swap_count = 0 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count 
def process_test_cases(test_cases):
    results = [] 
    for i in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        swap_count = bubble_sort(arr)
        results.append(swap_count)
    return results 
T = int(input())
results = process_test_cases(T)
for result in results:
    print(result)
