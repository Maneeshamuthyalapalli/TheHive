# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_frequencies(arr, queries):
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1 
    results = []
    for x in queries:
        results.append(frequency_map.get(x, 0))
    return results 
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = [int(input()) for _ in range(Q)]
results = find_frequencies(arr, queries)
for result in results:
    print(result)
