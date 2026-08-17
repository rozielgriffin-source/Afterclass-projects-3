num = int(input("Enter a number: "))

original = num
digits = len(str(num))
total = 0

for i in range(digits):
    digit = num % 10
    total += digit ** digits
    num //= 10

    if num == 0:
        break

if total == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")