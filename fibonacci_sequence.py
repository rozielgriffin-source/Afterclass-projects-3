num = int(input("Enter how many Fibonacci numbers: "))

a = 0
b = 1

for i in range(num):
    print(a)

    next_num = a + b
    a = b
    b = next_num

    if i == num - 1:
        break