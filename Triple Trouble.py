def find_unique_element(arr):
    result = 0
    for i in range(32):
        bit_sum = 0
        for num in arr:
            if num & (1 << i):
                bit_sum += 1
        if bit_sum % 3 != 0:
            result |= (1 << i)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result 
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(find_unique_element(arr))
main()
