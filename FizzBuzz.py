#!/usr/bin/python3
def fizzbuzz_loop(end_value: int):
    end_value += 1
    for num in range(1, end_value):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz") 
        else:
            print(num)


if __name__ == "__main__":
    # itertools
    # namedTuple?
    # defaultDict? just for fun
    fizzbuzz_loop(33)

