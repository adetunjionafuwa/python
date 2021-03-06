# ----------Task------------
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input:
# The first line has a double, mealCost (the cost of the meal before tax and tip).
# The second line has an integer, tipPercent (the percentage of mealCost being added as tip).
# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).


#-------Solution--------

def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost + (meal_cost * (tip_percent/100))+ (meal_cost * (tax_percent/100))))

if __name__ == '__main__':
    
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)