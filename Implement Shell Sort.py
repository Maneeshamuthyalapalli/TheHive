# Enter your code here. Read input from STDIN. Print output to STDOUT
def shell_sort(arr):
    n = len(arr)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i 
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap 
            arr[j] = temp 
        print(" ".join(map(str, arr)))
        gap //= 2 
n = int(input())
arr = list(map(int, input().split()))
shell_sort(arr)
