def WouldYouRather():
    print ("Welcome to Would You Rather!")
    print ("Here is your first choice!")
    print ("Type 1 or 2 and hit 'Enter'.")
#First question
    print("Would you rather drink ketchup, or drink pickel juice?")
    answer = input()
    print(answer)
#Second question
    if answer == ("1"):
        print("Would you rather have a short day of school with a lot of homework, or have a long day of school with not a lot of homework?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather have a short day of school with a lot of homework, or have a long day of school with not a lot of homework?")
        answer = input()
        print(answer)
#Third question
    if answer == ("1"):
        print("Would you rather go to school for the whole year, or summer school?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather go to school for the whole year, or summer school?")
        answer = input()
        print(answer)
#Fourth question
    if answer == ("1"):
        print("Would you rather be famous when you are alive but forgotten when you die, or unknown when you are alive but famous when you are dead?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather be famous when you are alive but forgotten when you die, or unknown when you are alive but famous when you are dead?")
        answer = input()
        print(answer)
#Fifth question
    if answer == ("1"):
        print("Would you rather have the power to fly, or have super strength?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather have the power to fly, or have super strength?")
        answer = input()
        print(answer)
#Sixth question
    if answer == ("1"):
        print("Would you rather travel for a year to places you have already been to, or travel for a week to places you've never been to?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather travel for a year to places you have already been to, or travel for a week to places you've never been to?")
        answer = input()
        print(answer)
#Seventh question
    if answer == ("1"):
        print("Would you rather play 1 video game all day or play 100 video games for 10 minutes each?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather play 1 video game all day or play 100 video games for 10 minutes each?")
        answer = input()
        print(answer)
#Eigth question
    if answer == ("1"):
        print("Would you rather always be 10 minutes late or always be 20 minutes early?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather always be 10 minutes late or always be 20 minutes early?")
        answer = input()
        print(answer)
#Ninth question
    if answer == ("1"):
        print("Would you rather never use social media sites / apps again or never watch another movie or TV show?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather never use social media sites / apps again or never watch another movie or TV show?")
        answer = input()
        print(answer)
#Tenth question
    if answer == ("1"):
        print("Would you rather live without the internet or live without AC and heating?")
        answer = input()
        print(answer)
    elif answer == ("2"):
        print("Would you rather live without the internet or live without AC and heating?")
        answer = input()
        print(answer)

    else:
        print ("You didn't pick 1 or 2! Try again.")
        WouldYouRather()
