
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n1=name1.lower()
n2=name2.lower()
n3=n1+n2
t=n3.count("t")
r=n3.count("r")
u=n3.count("u")
e=n3.count("e")
true=t+r+u+e
l=n3.count("l")
o=n3.count("o")
v=n3.count("v")
e=n3.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
love_score1=int(love_score)
if love_score1<10 or love_score1>90:
    print(f"Your score is {love_score1},you go together like coke and mentos.")
elif love_score1>40 and love_score1<50:
    print(f"Your score is {love_score1},you are alright together.")
else:
    print(f"Your score is {love_score1}.")
