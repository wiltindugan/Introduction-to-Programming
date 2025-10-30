answer=input("what is the capital of france?")
if answer.lower()=="paris":
    print("the answer is correct")
else:
    print("wrong")
quiz={
    "France":"Paris",
    "Germany":"Berlin",
    "Luxembourg":"Luxembourg City",
    "Croatia":"Zagreb",
    "Sanmarino":"San Marino",
    "Iceland":"Reykjavik",
    "lithuania":"Vilnius",
    "Monaco":"Monaco",
    "Poland":"Warsaw",
    "Slovakia":"Bratislava"
}
score=0
for country, capital in quiz.items():
    answer=input(f"What is the capital of {country} ")
    if answer.lower()==capital.lower():
        print("Correct!")
        score+=1
    else:
        print(f"nope wrong! The correct answer is {capital}.")
print(f"Your total score is {score} out of {len(quiz)}.")
