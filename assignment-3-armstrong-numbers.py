number = input("Please enter a number to check if it's an Armstrong Number : ")

len_num = len(number)

list_num = list(number)

armstrong = 0

if number.isalpha():
    print("Do not use any entries other than numeric values")
    
elif number.startswith("-"):
    print("Please enter a positive number")
    
elif ("." in list_num) or ("," in list_num):
    print("Please enter an integer number")
    
else:
    for i in list_num:
        armstrong += int(i) ** len_num
        
    if int(number)==armstrong:
        print("{} is an Armstrong number".format(int(number)))
    else:   
        print("{} is not an Armstrong number".format(int(number)))