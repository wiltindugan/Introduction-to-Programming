names=["Jake","Zac","Ian","Ron","Sam","Dave",]
search_name=input("Enter the name your searching for: ")
if search_name in names:
    print(f"{search_name} is found on the list above!!!")
else:
    print(f"{search_name} is not found in the list above!!!")