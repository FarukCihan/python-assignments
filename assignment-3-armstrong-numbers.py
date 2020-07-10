while True:
    number = input("Please enter a number to check if it's an Armstrong Number : ")

    len_num = len(number)

    list_num = list(number)

    armstrong = 0

    if number.isdecimal():
        for i in list_num:
            armstrong += int(i) ** len_num
            
        if int(number)==armstrong:
            print("{} is an Armstrong number".format(int(number)))
        else:   
            print("{} is not an Armstrong number".format(int(number)))
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")