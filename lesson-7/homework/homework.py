1.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
2.
def digit_sum(k):
    return sum(int(r) for r in str(abs(k)))
3.
def print_powers_of_two(N):
    k = 0
    while 2 ** k <= N:
        print(2 ** k)
        k += 1
