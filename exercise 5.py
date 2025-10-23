month_days={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
month=int(input("Enter month number (1-12): "))
if 1 <= month <= 12:
    if month == 2:
        leap=input("Is it leap year? (yes/no): ").lower()
        if leap == 'yes':
            print("Febuary has 29 days if its a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")
else:
    print("Thats an invalid month number!. Please enter a number between 1 and 12!!")