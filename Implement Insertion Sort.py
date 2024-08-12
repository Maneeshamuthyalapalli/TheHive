# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertion_sort(arr, N):
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1]=key
        print(' '.join(map(str, arr)))
def main():
    N = int(input()) 
    arr = list(map(int, input().split()))
    insertion_sort(arr, N)
if __name__ == "__main__":
    main()
