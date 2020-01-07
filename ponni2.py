maximum = int(input(" Enter the Max Value : "))
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("Even Numbers from 1 to {0} = {1}".format(number, total))
