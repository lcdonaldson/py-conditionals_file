# square each number from 1 - 10 and print the result.

num = 1

while num < 11:
  sqr = num ** 2
  print(sqr)
  num += 1


# simple interest

principle=float(input("starting amount in dollars:"))
time=int(input("time(in years):"))
rate=float(input("what rate?:"))
simple_interest=(principle*time*rate)/100
print("The interest in dollars = :",simple_interest)


# compund interest

def main():
    balance = float(input("Starting Balance: $ "))
    intRate = float(input("Interest Rate (%) : "))
    years = int(input("Years: "))
    newBalance = interestEquation(balance, intRate, years)

    print ("New balance:  $%.2f"  %(newBalance))
    
def interestEquation(bal, int, yrs):
    newBal = bal
    for i in range(yrs):
        newBal = newBal + newBal * int/100
    return newBal

main()
