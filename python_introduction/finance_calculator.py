#Financial calculator

#User input for financial details
mnth_inc = int(input("Enter your monthly income:"))
mnth_exp = int(input("Enter your total monthly expenses:"))

#Calculate monthly savings
mnth_sav = mnth_inc - mnth_exp

#Project Annual Savings
#ann_interest = 5 annual interest rate of 5%
projected_savings = mnth_sav * 12 + (mnth_sav * 12 * 0.05)

#Output Results
print("Your monthly savings are", mnth_sav)
print("Projected savings after one year, with interest, is:", projected_savings)
