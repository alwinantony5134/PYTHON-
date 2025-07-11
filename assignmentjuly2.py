# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def primes_within_limit(limit):
#     primes = []
#     for number in range(2, limit + 1):
#         if is_prime(number):
#             primes.append(number)
#     return primes

# # Input from the user
# limit = int(input("Enter the upper limit: "))
# prime_numbers = primes_within_limit(limit)

# print(f"Prime numbers up to {limit}:")
# print(prime_numbers)
