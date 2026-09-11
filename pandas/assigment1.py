# ---------------------------------------------------------------
# q1 answer  -- Assignment 1.1: print your name three times
# ---------------------------------------------------------------

name = input("Enter your name: ")

for _ in range(3):          
    print(name)


# ---------------------------------------------------------------
# q2 answer  -- Assignment 2.1 and 2.2
# ---------------------------------------------------------------

# 2.1 Add three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sum =", a + b + c)


# 2.2 Concatenate three strings
p = input("Enter first string: ")
q = input("Enter second string: ")
r = input("Enter third string: ")
print("Concatenated string =", p + q + r)


# ---------------------------------------------------------------
# q4 answer  -- Assignment 4.1, 4.2, 4.3
# ---------------------------------------------------------------

for base in (7, 9):
    print(f"\nTable of {base}")
    for i in range(1, 11):
        print(f"{base} * {i} = {base * i}")


# 4.2 Table of n
n = int(input("\nEnter a number for its table: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# 4.3 Sum of 1 to n
n = int(input("Enter n to sum 1..n: "))
total = 0
for i in range(1, n + 1):    
    total += i
print("Sum is -->", total)



# ---------------------------------------------------------------
# q5 answer  -- Assignment 5.1, 5.2, 5.3
# ---------------------------------------------------------------

# 5.1 Maximum of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Max -->", max(a, b, c))


n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:    
        total += i
print("Sum (divisible by 7 and 9) -->", total)


# 5.3 Sum of all primes from 1 to n
n = int(input("Enter n to sum primes up to it: "))
total = 0
for num in range(2, n + 1):      
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break                   
    if is_prime:
        total += num
print("Sum of primes -->", total)


# ---------------------------------------------------------------
# q6 answer  -- Assignment 6.1, 6.2
# ---------------------------------------------------------------

# 6.1 Function: sum of odd numbers from 1 to n
def add_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total        

print("add_odd(10) -->", add_odd(10))    # 25
print("add_odd(20) -->", add_odd(20))    # 100

# 6.2 Functions: sum of primes from 1 to n
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True                     

def add_primes(n):
    return sum(i for i in range(2, n + 1) if is_prime(i))

print("add_primes(20) -->", add_primes(20))    # 77
print("add_primes(50) -->", add_primes(50))    # 328
