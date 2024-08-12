def insertion_sort_indices(arr):
    indices = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key 
        indices.append(j + 1)
    return indices 
def main():
    T = int(input())
    results = [] 
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        result = insertion_sort_indices(arr)
        results.append(' '.join(map(str, result)))
    for result in results:
        print(result)
if __name__ == "__main__":
    main()
