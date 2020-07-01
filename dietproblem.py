#import pandas and pulp packages

from pulp import *
import pandas as pd

#read all data from excelsheet
food_data = pd.read_excel("C:/Users/kastu/Documents/R Scripts/HW11/diet.xls",header = 0)

#This is a list of all foods that will form the diet
food = food_data[0:64]

#Now food is a pandas dataframe. But we will need to convert this to a list for future usage
food_list = food.values.tolist()

#get minimum and maximum nutrient values from the food_data dataframe read above
min_nutrients = food_data[65:66].values.tolist()[0][3:]
max_nutrients = food_data[66:67].values.tolist()[0][3:]

# append collection of contraints for each column
nutrients = []
for j in range(0,11):
    nutrients.append(dict([(x[0], float(x[j+3])) for x in food_list]))

#cost dictionary for each food
cost = dict([(x[0], float(x[1])) for x in food_list])

lp_prob = LpProblem('Diet Problem', LpMinimize)

food_names = [i[0] for i in food_list]

# since we can't eat negative amounts of food, we specify lower limit = 0
food_variables = LpVariable.dicts("Foods", food_names, 0)
#If the food is eaten, then 1 else 0
chosen_food_variables = LpVariable.dicts("food_select",food_names,0,1,LpBinary)

#Now lets create the objective function
lp_prob += lpSum([cost[f] * food_variables[f] for f in food_names])

# ---------------------------Adding constraints for foods - Solution for Part 1 ---------------

for i in range(0,11):
    condition = lpSum([nutrients[i][j] * food_variables[j] for j in food_names])
    lp_prob += condition >= min_nutrients[i]
    lp_prob += condition <= max_nutrients[i]

lp_prob.solve()

print("-------------------------Part 1---------------------")
print()
print("Optimization Solution for the diet problem - Part 1")
for k in lp_prob.variables():
    if k.varValue > 0 and str(k).find('Chosen'):
        print(str(k) + ":" + str(k.varValue) + "units")

print("Total cost of diet = $%.2f" % value(lp_prob.objective))

print("--------------------------Part 2 ----------------------")

for food in food_names:
    lp_prob += food_variables[food] >= 0.1 * chosen_food_variables[food]

for food in food_names:
    lp_prob += chosen_food_variables[food] >= food_variables[food] * 0.000001

#this is part B
lp_prob += chosen_food_variables['Frozen Broccoli'] + chosen_food_variables['Celery, Raw'] <= 1

#this is part C
lp_prob += chosen_food_variables['Roasted Chicken'] + chosen_food_variables['Poached Eggs'] + \
  chosen_food_variables['Scrambled Eggs'] + chosen_food_variables['Frankfurter, Beef'] + \
  chosen_food_variables['Kielbasa,Prk'] + chosen_food_variables['Hamburger W/Toppings'] + \
  chosen_food_variables['Hotdog, Plain'] + chosen_food_variables['Pork'] + chosen_food_variables['Sardines in Oil'] + \
  chosen_food_variables['Bologna,Turkey'] + chosen_food_variables['Ham,Sliced,Extralean'] + chosen_food_variables['Chicknoodl Soup'] +\
  chosen_food_variables['White Tuna in Water'] + chosen_food_variables['Pizza W/Pepperoni'] + chosen_food_variables['Neweng Clamchwd'] >= 3

lp_prob.solve()
print()
print("Optimization Solution for the diet problem ---- Part 2")
for k in lp_prob.variables():
    if k.varValue > 0 and str(k).find('Chosen'):
        print(str(k) + ":" + str(k.varValue) + "units")

print("Total cost of diet = $%.2f" % value(lp_prob.objective))
