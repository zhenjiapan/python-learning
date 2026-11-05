## 6.100A PSet 1: Part A: Saving for a House
## Name: Steven Pan
## Date: Tue 22 Sep 2026

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input('Enter your yearly salary:'))
portion_saved = float(input('Enter the percent of your salary save, as a decimal:'))
cost_of_dream_home = float(input('Enter the cost of your dream home:'))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < cost_of_dream_home*portion_down_payment:
    months += 1
    amount_saved += yearly_salary*portion_saved/12 + amount_saved*r/12
print('Number of months:',months)
