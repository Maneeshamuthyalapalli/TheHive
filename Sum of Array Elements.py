# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_of_array_elements():
    import sys 
    input = sys.stdin.read 
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1 
    results = [] 
    for _ in range(T):
        N = int(data[index])
        index += 1
        sum_elements = 0
        for _ in range(N):
            sum_elements += int(data[index])
            index += 1 
        results.append(sum_elements)
    for result in results:
        print(result)
sum_of_array_elements()
       

