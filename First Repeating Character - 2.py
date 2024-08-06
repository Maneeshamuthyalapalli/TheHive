# Enter your code here. Read input from STDIN. Print output to STDOUT
def first_repeating_character(s):
    seen = set()
    for char in s:
        if char in  seen:
            return char
        seen.add(char)
    return '.'
def main():
    import sys 
    input = sys.stdin.read 
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        string = data[i]
        results.append(first_repeating_character(string))
    for result in results:
        print(result)
if __name__ == "__main__":
    main()
