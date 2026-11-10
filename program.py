for i in range(1, 101):
    if i%15 == 0: # El 15 es igual a multiplicar 3*5
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)