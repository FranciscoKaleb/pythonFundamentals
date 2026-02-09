
# List within list

# the List contains the following data about a grocery stores' sales by the month of November(30 days)
# Each item is represented as a list containing:
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
november_sales = [
    ['Chicken', 150, 'Food', 'Standard VAT', 804, 1200],
    ['Hotdog', 50, 'Food', 'Standard VAT', 1200, 2000],
    ['Rice', 40, 'Food', 'Zero-Rated', 1500, 2500],
    ['Bread', 30, 'Food', 'Standard VAT', 900, 1500],
    ['Soap', 25, 'Non-Food', 'Standard VAT', 600, 1000],
    ['Shampoo', 120, 'Non-Food', 'Standard VAT', 450, 800],
    ['Vitamins', 300, 'Health', 'VAT-Exempt', 300, 600],
    ['Medicine', 500, 'Health', 'VAT-Exempt', 200, 400],
    ['Notebook', 80, 'Stationery', 'Standard VAT', 750, 1200],
    ['Pen', 15, 'Stationery', 'Standard VAT', 1000, 1500],
    ['Pencil', 10, 'Stationery', 'Standard VAT', 1100, 1600],
    ['Eraser', 5, 'Stationery', 'Standard VAT', 950, 1400],
    ['Juice', 60, 'Food', 'Standard VAT', 850, 1300],
    ['Soda', 40, 'Food', 'Standard VAT', 950, 1400],
    ['Vegetables', 70, 'Food', 'Zero-Rated', 1300, 2000],
    ['Fruits', 90, 'Food', 'Zero-Rated', 1250, 1900],
    ['Toothpaste', 80, 'Non-Food', 'Standard VAT', 500, 900],
    ['Toothbrush', 60, 'Non-Food', 'Standard VAT', 550, 950],
    ['Bandages', 150, 'Health', 'VAT-Exempt', 400, 700],
    ['Calculator', 200, 'Stationery', 'Standard VAT', 300, 500],
] 
# with the given data on november sales, get the following information:

# easy:
# - [1] total number of items sold
# - [2] total number of sold items per category
# - [3] total sales amount
# - [4] total sales amount per category
# - [5] average price of items per category


print('-----------------[ [1] total number of items sold]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

# expected output
# Total number of items sold: 15854
items_sold = 0

for item in november_sales:
    items_sold = items_sold + item[4]
print(f'Total number of items sold: {items_sold}')
print()

print('-----------------[ [2] total number of sold items per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here
# we are finding quantity here

food_sold = 0
non_food_sold = 0
health_sold = 0
stationery_sold = 0

for item in november_sales:
    if item[2] == 'Food':
        food_sold = food_sold + item[4]
    elif item[2] == 'Non-Food':
        non_food_sold = non_food_sold + item[4]
    elif item[2] == 'Health':
        health_sold = health_sold + item[4]
    else:
        stationery_sold = stationery_sold + item[4]
        
print(f'food sold: {food_sold}')
print(f'non-food sold: {non_food_sold}')
print(f'health sold: {health_sold}')
print(f'stationery sold: {stationery_sold}')
print(f'total sold: {items_sold}')
print()

print('-----------------[ [3] total sales amount]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here
total_sales = 0
for item in november_sales:
    total_sales = total_sales + item[1]*item[4]

print(f'total sales: {total_sales}')
print()



print('-----------------[ [4] total sales amount per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here
food_sales = 0
non_food_sales = 0
health_sales = 0
stationery_sales = 0

for item in november_sales:
    if item[2] == 'Food':
        food_sales = food_sales + item[1]*item[4]
    elif item[2] == 'Non-Food':
        non_food_sales = non_food_sales + item[1]*item[4]
    elif item[2] == 'Health':
        health_sales = health_sales + item[1]*item[4]
    else:
        stationery_sales = stationery_sales + item[1]*item[4]
        
total_sales = food_sales + non_food_sales + health_sales + stationery_sales
    
print(f'food sales: {food_sales}')
print(f'non-food sales: {non_food_sales}')
print(f'health sales: {health_sales}')
print(f'stationery sales: {stationery_sales}')
print(f'total sales: {total_sales}')
print()

print('-----------------[ [5] average price of items per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

food_price_sum = 0
food_count = 0

non_food_price_sum = 0
non_food_count = 0

health_price_sum = 0
health_count = 0

stationery_price_sum = 0
stationery_count = 0

for item in november_sales:
    if item[2] == 'Food':
        food_price_sum = food_price_sum + item[1]
        food_count = food_count + 1
    elif item[2] == 'Non-Food':
        non_food_price_sum = non_food_price_sum + item[1]
        non_food_count = non_food_count + 1
    elif item[2] == 'Health':
        health_price_sum = health_price_sum + item[1]
        health_count = health_count + 1
    else:
        stationery_price_sum = stationery_price_sum + item[1]
        stationery_count = stationery_count + 1

food_price_average = food_price_sum/food_count
non_food_average = non_food_price_sum/non_food_count
health_average = health_price_sum/health_count
stationery_average = stationery_price_sum/stationery_count

print(f'food price average: {food_price_average}')
print(f'non-food price average: {non_food_average}')
print(f'health price average: {health_average}')
print(f'stationery price average: {stationery_average}')


price_list = [row[1] for row in november_sales]
print(min(price_list))