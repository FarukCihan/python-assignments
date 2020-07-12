fibo = []

for i in range(2): fibo.append(1)

for i in range(8): fibo.append(fibo[i]+fibo[i+1])

print("fibonacci numbers ->", fibo)
