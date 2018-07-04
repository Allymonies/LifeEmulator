import json
import readline
import industry_recipes
while True:
	print("What item would you like to view the recipe of?")
	item = input()
	print(json.dumps(industry_recipes.calculate_cost(item), indent=4, sort_keys=True))