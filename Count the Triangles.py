def count_triangles(rods):
    rods.sort()
    count = 0
    n = len(rods)
    for i in range(n - 2):
        k = i + 2 
        for j in range(i + 1, n - 1):
            while k < n and rods[i] + rods[j] > rods[k]:
                k += 1 
            count += k - j - 1 
    return count 
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    rods = list(map(int, input().split()))
    triangle_count = count_triangles(rods)
    results.append(str(triangle_count))
print("\n".join(results))
