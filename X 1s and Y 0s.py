def find_number(X, Y):
    MOD = 1000000007
    num = ((1 << X) - 1) << Y 
    return num % MOD 
def main():
    import sys
    input = sys.stdin.read 
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        X = int(data[2 * i - 1])
        Y = int(data[2 * i])
        results.append(str(find_number(X, Y)))
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
