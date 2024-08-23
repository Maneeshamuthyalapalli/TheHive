# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_repeated_numbers(arr, N):
    frequency = [0] * (N - 1)
    repeated = []
    for num in arr:
        if frequency[num - 1] == 1:
            repeated.append(num)
        else:
            frequency[num - 1] += 1
    repeated.sort()
    return repeated 
def main():
    import sys
    input = sys.stdin.read 
    data = input().split() 
    index = 0
    T = int(data[index])
    index += 1 
    results = []
    for _ in range(T):
        N = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + N]))
        index += N 
        repeated_numbers = find_repeated_numbers(arr, N)
        results.append(f"{repeated_numbers[0]} {repeated_numbers[1]}")
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
