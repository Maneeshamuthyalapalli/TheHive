def max_wins(team_a, team_b):
    team_a.sort()
    team_b.sort()
    i, j = 0, 0
    wins = 0
    n = len(team_a)
    while i < n and j < n:
        if team_a[i] > team_b[j]:
            wins += 1
            j += 1
        i += 1
    return wins 
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    team_a = list(map(int, input().split()))
    team_b = list(map(int, input().split()))
    result = max_wins(team_a, team_b)
    results.append(str(result))
print("\n".join(results))
