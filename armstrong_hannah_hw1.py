num = input("Enter a number:")
num = int(num)
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print(str(num) + " is a leap year.")
        else:
            print(str(num) + " is not a leap year.")
    else:
        print(str(num) + " is a leap year.")
else:
    print(str(num) + " is not a leap year.")
