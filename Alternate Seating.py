# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_seat_people(N, M, seats):
    i = 0
    count = 0
    while i < M:
        if seats[i] == 0:
            if (i == 0 or seats[i - 1] == 0) and (i == M-1 or seats[i+1] == 0):
                count += 1 
                i += 2
            else:
                i += 1
        else:
            i += 1 
    return "YES" if count >= N else "NO"
def main():
    N = int(input())
    M = int(input())
    seats = list(map(int, input().split()))
    result = can_seat_people(N, M, seats)
    print(result)
if __name__ == "__main__":
    main()
