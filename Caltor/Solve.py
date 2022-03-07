
a =100
num_right = []

for a in range(1,100):
    if int((a*a*a+23)/24) == ((a*a*a+23)/24):
        num_right.append(a)
        a = a-1

    else:
        a = a-1

print(num_right)
