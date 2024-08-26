# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 
def frequency_sort(arr):
    freq = Counter(arr)
    sorted_elements = sorted(arr, key=lambda x: (freq[x], x))
    return sorted_elements 
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = frequency_sort(arr)
    results.append(" ".join(map(str, sorted_arr)))
for result in results:
    print(result)
