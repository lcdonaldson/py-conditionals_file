//simple question and response inputs to simulate application logic

print("hello user")

myVar = input("Enter your location")

if(myVar == " Thatcher"):
    print("It isn't heaven but for now it's home")

elif(myVar == " Pima"):
    print("At least you're not in safford")

else:
    print("You might look into the Texas Hill Country")

myVar1 = input("Tell me your favorite food?")

if(myVar1 == " Steak"):
    print("You rock")

elif(myVar1 == " tex mex"):
    print("You should seek counseling")

else:
    print("Its not steak, but everyone's entitled to their own opinion")

myVar2 = input("Would you consider yourself a developer or designer?")

if(myVar2 == " developer"):
    print("Your site works awesome but it looks like atari from 1980")

elif(myVar2 == " designer"):
    print("Wow your site rocks! Just dont click the buttons")

else:
    print("You poor 'WordPress ninja' ")
print("")

print("Ok ok...enough chit chat, time for some real info")
myVar3 = input("Are you familiar with Pharmacogenetics? Y/N")

if(myVar3 == " Y"):
    print("Can I direct you to a fantastic website about getting the genetic testing done")

else:
    print("Please go to www.pharmacogenetics.com to learn some more")
    
myVar4 = input("Are you a physician or an individual seeking genetic testing?")

if(myVar4== " Physician"):
    print("Thank you for using Genecheck, we need to send you to our physician specific site now. click the following link http://www.docgene.com")

else:
    print("Excellent! Let's get you started")
    
myVar5 = input("Y /N?")

if(myVar5== " Y"):
    print("Please visit www.medxprime.com")

else:
    print("That's ok...lets find out how to help you here")
myVar6 = input("what would you like to know most about this topic")

if(myVar6== " Results"):
   print("medxprime labs offer state of the art DNA testing to check for genetic markers that indicate probabilites for the type of reactions your body might have to different medicines") 
