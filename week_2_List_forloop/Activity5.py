

# Activity: Lists within a List

# The list contains staff names and the money they have collected from people,

# now, the manager takes 17%, 
# unit head takes 10%, 
# staff takes 6% if the collection is 6000 and above, if its below 6000 then staff takes 5% 
# and the rest goes to the company.
# How much money goes to each party?

# print the total amount collected
# print the:
# managers portion
# unit head's portion
# company's portion
# staff's portion

names_payment = [
    ['John', 6700],
    ['Jane', 7200],
    ['Doe', 5600],
    ['Alice', 8100],
    ['Bob', 4500],
    ['Eve', 9000],
    ['Charlie', 6200],
    ['Dave', 7300],
    ['Faythe', 4800],
    ['Grace', 5900]
]

total = 0
manager_total = 0
unit_head_total = 0
company_total = 0

for x in names_payment:
    total = total + x[1]
    manager_total = manager_total + x[1]*0.17
    unit_head_total = unit_head_total + x[1]*0.1
    if x[1] >= 6000:
        company_total = company_total + x[1]*0.67
    else:
        company_total = company_total + x[1]*0.68

print(f'total: {total}')
print(f'manager: {manager_total}')
print(f'unit head: {unit_head_total}')
print(f'company: {company_total}')

for x in names_payment:
    if x[1] >= 6000:
        print(x[0] + ' ' + str(x[1]*0.06))
    else:
        print(x[0] + ' ' + str(x[1]*0.05))



# Expected output:

# total: 65300
# manager: 11101.0
# unit head: 6530.0
# company: 43959.0
# John 402.0
# Jane 432.0
# Doe 280.0
# Alice 486.0
# Bob 225.0
# Eve 540.0
# Charlie 372.0
# Dave 438.0
# Faythe 240.0
# Grace 295.0
    

    