def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_in_range(min_value, max_value):
    for num in range(min_value, max_value + 1):
        if is_prime(num):
            yield num

if __name__ == "__main__":
    N = int(input("Enter the minimum value (N): "))
    Z = int(input("Enter the maximum value (Z): "))

    if N > Z:
        N, Z = Z, N

    prime_generator = generate_primes_in_range(N, Z)
    primes = list(prime_generator)

    print("Prime numbers in the range:", primes)

