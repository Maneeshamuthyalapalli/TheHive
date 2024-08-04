# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_hollow_diamond():
    import sys 
    input = sys.stdin.read 
    data = input().split()
    T = int(data[0])
    cases = [int(data[i]) for i in range(1, T + 1)]
    for case_num in range(1, T + 1):
        N = cases[case_num - 1]
        print(f"Case #{case_num}:")
        for i in range(N//2 + 1):
            if i == 0:
                print(' ' * (N//2) + '*')
            else:
                print(' ' * (N//2 - i) + '*' + ' ' * (2 * i - 1) + '*')
        for i in range(N//2 - 1, -1, -1):
            if i == 0:
                print(' ' * (N//2) + '*')
            else:
                print(' ' * (N//2 - i) + '*' + ' ' * (2 * i - 1) + '*') 
print_hollow_diamond()
