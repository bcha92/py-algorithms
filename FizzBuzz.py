# FizzBuzz

def FizzBuzz(num): # Function format for FizzBuzz(num)
    if num % 3 == 0 & num % 5 == 0: # Outputs "FizzBuzz" for all multiples of 3 and 5
        print("FizzBuzz");
    elif num % 3 == 0: # Outputs "Fizz" for all multiples of 3
        print("Fizz");
    elif num % 5 == 0: # Outputs "Buzz" for all multiples of 5
        print("Buzz");
    else: # Outputs number for everything else
        print(num);

# FizzBuzz from 1 to 200
for i in range(1, 201):
    FizzBuzz(i);
