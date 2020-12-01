def fizzbuzz(n):
    for x in range(n):
        if x % 15 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)


print(fizzbuzz(16))