import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_in_range(N, Z):
    primes = [str(num) for num in range(max(2, N), Z + 1) if is_prime(num)]
    return " ".join(primes)

# Генеруємо випадкові значення N і Z
import random
N = random.randint(1, 100)
Z = random.randint(N, N + 100)

result = generate_primes_in_range(N, Z)
print(result)
