def find_number(X, Y):
    MOD = 1000000007
    num = (1 << X) | (1 << Y)
    return num % MOD 
def main():
    import sys
    input = sys.stdin.read 
    data = input().split() 
    T = int(data[0])
    results = [] 
    index = 1 
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index + 1])
        results.append(str(find_number(X, Y)))
        index += 2 
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
