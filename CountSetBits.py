def count_set_bits(n):
    return bin(n).count('1')
def main():
    import sys
    input = sys.stdin.read 
    data = input().split()
    T = int(data[0])
    results = [] 
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(str(count_set_bits(N)))
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
