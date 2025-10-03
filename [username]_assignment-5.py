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
