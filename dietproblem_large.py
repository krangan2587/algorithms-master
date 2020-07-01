from pulp import *
import pandas as pd

#read all data from excelsheet
large_diet_data = pd.read_excel("C:/Users/kastu/Documents/R Scripts/HW11/diet_large.xls",skiprows = 1,header = 0)

#This is a list of all foods that will form the dietcost
large_diet = large_diet_data[0:7146]

#replace nan in the dataframe with 0
#convert large_diet which is a pandas dataframe into a list
large_diet_list = large_diet.fillna(0).values.tolist()

#get minimum and maximum nutrient values
min_nutrients = large_diet_data[7147:7148].fillna(0).values.tolist()[0][1:]
max_nutrients = large_diet_data[7149:7151].fillna(0).values.tolist()[0][1:]

nutrient_names = list(large_diet_data)
nutrient_count =len(nutrient_names) -1
# the -1 is to remove the first column which is not a nutrient

# append collection of contraints for each column
nutrients = []
for j in range(0,nutrient_count):
    nutrients.append(dict([(x[0], float(x[j+1])) for x in large_diet_list]))

#cost dictionary for each food
cost = dict([(x[0], float(x[nutrient_names.index('Cholesterol')])) for x in large_diet_list])

lp_prob = LpProblem('Diet Problem', LpMinimize)

food_names = [i[0] for i in large_diet_list]

# since we can't eat negative amounts of food, we specify lower limit = 0
food_variables = LpVariable.dicts("Foods", food_names, 0)
#If the food is eaten, then 1 else 0
chosen_food_variables = LpVariable.dicts("food_select",food_names,0,1,LpBinary)

#Now lets create the objective function
lp_prob += lpSum([cost[f] * food_variables[f] for f in food_names])

# ---------------------------Adding constraints for foods - Solution for the large diet problem ---------------

for i in range(0,nutrient_count):
    condition = lpSum([nutrients[i][j] * food_variables[j] for j in food_names])
    lp_prob += condition >= min_nutrients[i]
    lp_prob += condition <= max_nutrients[i]

lp_prob.solve()

print()
print("Optimization Solution for the large diet problem - Part 1")
for k in lp_prob.variables():
    if k.varValue > 0 and str(k).find('Chosen'):
        print(str(k) + ": " + str(k.varValue) + "units")

print("Total Cholesterol in diet = $%.2f" % value(lp_prob.objective))