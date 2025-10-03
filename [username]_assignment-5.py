print("=== challenge 1: Collatz Conjecture ===")
n = int(input(f"Enter starting number: "))
print(f"Sequence: {n}", end=" ")
count = 0

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3) + 1
    print(int(n),end=" ")
    count +=1
print()
print(f"Steps: {count} \n")

print("=== challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {num-1}")
for i in range(2, num-1):
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        break
    i += 1
else:
    print(f"{num} is prime!")
print()

print("Multiplication Table:")
for row in range(1,11):
    print(f" {row:5}", end = "")

for row in range(1,11):
    print(f"\n{row:3}", end= "")
    for col in range(1,11):
        print(f"{(row * col):3}", end="")
        print("   ", end="")

