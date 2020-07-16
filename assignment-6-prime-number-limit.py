n = int(input("Please enter a integer number to list Prime Numbers : "))

prime = []

for i in range(2,n+1):
    if i==2 or i==3 or i==5 or i==7:
        prime.append(i)
    elif i%2 and i%3 and i%5 and i%7:
        prime.append(i)

print(prime)
