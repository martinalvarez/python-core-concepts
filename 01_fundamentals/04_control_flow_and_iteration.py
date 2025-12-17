"""
Focus: Advanced loops and the 'else' clause.
"""

def find_prime(n: int):
    # The 'for...else' clause: Runs ONLY if the loop didn't 'break'
    # Great for search patterns.
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime (found factor {i})")
            break
    else:
        print(f"{n} is a prime number!")

def ternary_operator():
    status = 200
    # Concise conditional assignment
    message = "Success" if status == 200 else "Error"
    print(f"Status: {message}")

if __name__ == "__main__":
    find_prime(7)
    find_prime(10)
    ternary_operator()