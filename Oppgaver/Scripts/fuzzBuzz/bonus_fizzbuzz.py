def bonus_fizzBuzz (n):
    for i in range(1, n + 1): # Loop gjennom tallene fra 1 til n
        if i % 3 == 0 and i % 5 == 0: # Sjekk om tallet er delelig med både 3 og 5
            print("FizzBuzz")
        elif i % 3 == 0: # Sjekk om tallet er delelig med 3
            print("Fizz")
        elif i % 5 == 0: # Sjekk om tallet er delelig med 5
            print("Buzz")
        else:
            print(i)
# Kjør funksjonen med n = 100
bonus_fizzBuzz(100)