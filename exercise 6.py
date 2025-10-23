correct_password="wil0523"
max_attempts=3
attempts=0
while attempts < max_attempts:
    password=input("Enter password:")
    attempts+=1
    if password==correct_password:
        print("Password accepted, welcome Wil!")
        break
    else:
        remaining=max_attempts-attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempts left.")
        else:
            print("Maximum attempts reached, the authorities have now been notified. R U N!")