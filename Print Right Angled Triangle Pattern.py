# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_triangle_pattern():
    import sys 
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    cases = [int(data[i]) for i in range(1, T + 1)]
    for case_num in range(1, T + 1):
        N = cases[case_num - 1]
        print(f"Case #{case_num}:")
        for i in range(1, N + 1):
            print(' '* (N - i) + '*' * i)
print_triangle_pattern()
