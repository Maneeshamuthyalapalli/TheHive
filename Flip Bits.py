def count_flipped_bits(A, B):
    return bin(A ^ B).count('1')
def main():
    import sys
    input = sys.stdin.read 
    data = input().split() 
    T = int(data[0])
    results = []
    index = [] 
    index = 1
    for _ in range(T):
        A = int(data[index])
        B = int(data[index + 1])
        results.append(str(count_flipped_bits(A, B)))
        index += 2
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
