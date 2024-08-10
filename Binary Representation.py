# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    binary_representation = bin(N)[2:]
    results.append(binary_representation)
print('\n'.join(results))
