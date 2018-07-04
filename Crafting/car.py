import json
import industry_recipes
industry_recipes.add_machine("manual")

models = [
	{
		"name":"semi",
		"ingredients": [
			"semi_frame",
			"vehicle_tire",
			"vehicle_tire",
			"vehicle_tire",
			"vehicle_tire",
			"vehicle_frame",
			"vehicle_frame",
			"vehicle_frame",
			"vehicle_frame",
			"vehicle_radiator",
			"vehicle_battery",
			"vehicle_engine",
			"vehicle_alternator",
			"vehicle_fuel_tank",
			"vehicle_trunk",
			"vehicle_exhaust",
		]
	}
]

for model in models:
	industry_recipes.add_recipe("manual",model["name"],model["ingredients"])

industry_recipes.index_recipes()
print(json.dumps(industry_recipes.calculate_cost("semi"), indent=4, sort_keys=True))