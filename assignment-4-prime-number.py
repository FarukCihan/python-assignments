while True:
    number = int(input("Please enter a integer number to check if it's a Prime Number : "))
    
    if number==0 or number==1:
        print("{} is not a prime number".format(number))
    
    elif number==2 or number==3 or number==5 or number==7:
        print("{} is a prime number".format(number))
    
    elif not(number%2 and number%3 and number%5 and number%7):
        print("{} is not a prime number".format(number))
        
    elif number%number==0:
        print("{} is a prime number".format(number))