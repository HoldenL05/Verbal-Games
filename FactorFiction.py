def FactorFiction:
    print("Welcome to Fact or Fiction!")
    print("A myth of fact will be presented to you.")
    print("Type fact or fiction for whatever you think the fact or fiction presented to you is.")

#First Myth or Fact

print("If you are stung by a jellyfish while swimming in the ocean, you should have someone urinate on the sting.")
answer = input()
print(answer)

if answer == ("fact"):
    print("Sorry. You are wrong.")
elif answer == ("fiction"):
    print("You got that right!")

print("Eating bananas will attract mosquitoes, while eating garlic will repel them.") 
answer = input()
print("answer")