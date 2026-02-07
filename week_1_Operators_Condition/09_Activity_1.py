
# Deductions:

# [1] GSIS 
    # 9% of monthly salary 
# [2] PhilHealth 
    # For monthly income ₱10,000 and below, total contribution is ₱250; 
    # for ₱10,000.01 to ₱99,999.99 ->  2.5% of monthly salary;        
    # for ₱100,000 and above, it is ₱5,000.
# [3] Pag-IBIG
    # 1500 below monthly salary -> 1% of monthly Salary
    # 1501 - 10000 -> 2% of monthly Salary
    # 10000 and above -> fixed 200
# [4] Withholding tax
    # 0 - 20832 -> 0%
    # 20833 - above -> 20% of the excess over 20832
    # theres other condition for higher salary but for this activity we will just use this
    

# Create a program that calculates the net pay of a government employee after deductions.
# use given above deduction rules

print('Enter your monthly wage:')
monthly_wage = float(input())

GSIS_deduction = 0.09 * monthly_wage

Philhealth_deduction = 0 # initialize variable

if monthly_wage <= 10000:
    Philhealth_deduction = 250
elif monthly_wage > 10000 and monthly_wage < 100000:
    Philhealth_deduction = 0.025 * monthly_wage
else:
    Philhealth_deduction = 5000




PagIBIG_deduction = 0
if monthly_wage <= 1500:
    PagIBIG_deduction = 0.01 * monthly_wage
elif monthly_wage > 1500 and monthly_wage <= 10000:
    PagIBIG_deduction = 0.02 * monthly_wage
else:
    PagIBIG_deduction = 200
    
Withholding_tax_deduction = 0
if monthly_wage > 20832:
    Withholding_tax_deduction = 0.20 * (monthly_wage - 20832)
    
net_pay = monthly_wage - (GSIS_deduction + Philhealth_deduction + PagIBIG_deduction + Withholding_tax_deduction)


print(f'GSIS Deduction: {GSIS_deduction}')
print(f'PhilHealth Deduction: {Philhealth_deduction}')
print(f'Pag-IBIG Deduction: {PagIBIG_deduction}')
print(f'Withholding Tax Deduction: {Withholding_tax_deduction}')
print(f'Net pay: {net_pay}')



# TEST CASE for 20k
# Enter your monthly wage:
# 20000

# GSIS Deduction: 1800.0
# PhilHealth Deduction: 500.0
# Pag-IBIG Deduction: 200
# Withholding Tax Deduction: 0
# Net pay: 17500.0


# TEST CASE for 100k
# Enter your monthly wage:
# 100000

# GSIS Deduction: 9000.0
# PhilHealth Deduction: 5000
# Pag-IBIG Deduction: 200
# Withholding Tax Deduction: 15833.6
# Net pay: 69966.4