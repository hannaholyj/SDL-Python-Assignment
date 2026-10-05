for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0: #if number divisable by 5 and 3 (fizzbuzz)
        print(number,": FizzBuzz")
    elif number % 3 == 0: #if divisable by 3 = Fizz
        print(number,": Fizz")
    elif number %5 ==0: #divisable by 5 Buzz
        print(number,": Buzz")
    else :
        print(number,":", number)
    