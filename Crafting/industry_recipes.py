recipes = {}
recipes["advanced_assembler"] = {}
recipes["standard_assembler"] = {}
recipes["basic_assembler"] = {}
recipes["dehumidifier"] = {}
recipes["component_manipulator"] = {}
recipes["smeltry"] = {}
recipes["chemical_assembler"] = {}
recipes["metal_caster"] = {}
recipes["extractor"] = {}
indexes = {}
#Advanced Assembler Recipes
recipes["advanced_assembler"]["accurate_autobow"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"bow",
		"polymer_silk_leather",
		"compound_wood"
	]
}
recipes["advanced_assembler"]["advanced_assembler"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["advanced_assembler"]["basic_assembler"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["advanced_assembler"]["belt_teleporter"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 16
}
recipes["advanced_assembler"]["car_frame"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"standard_vehicle_chassis",
		"dense_mesh"
	]
}
recipes["advanced_assembler"]["combustion_generator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_generator_scrap",
		"industrial_scrap",
		"industrial_scrap"
	] * 4
}
recipes["advanced_assembler"]["comfort_bed_10"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"spring_box",
		"spring_box"
	]
}
recipes["advanced_assembler"]["comfort_bed_9"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"spring_box",
	]
}
recipes["advanced_assembler"]["component_manipulator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 32
}
recipes["advanced_assembler"]["dryer"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"iron_block",
		"moldable_alloy_frame",
		"metal_spring"
	]
}
recipes["advanced_assembler"]["electric_stove"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"furnace",
		"conductive_mesh",
		"sheet_metal"
	]
}
recipes["advanced_assembler"]["fiber_glass"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"glass_crystals",
		"wool",
		"metalic_fiber"
	]
}
recipes["advanced_assembler"]["hydro_generator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_generator_scrap",
		"industrial_scrap",
		"industrial_scrap"
	] * 4
}
recipes["advanced_assembler"]["oil_generator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_generator_scrap",
		"industrial_scrap"
	] * 16
}
recipes["advanced_assembler"]["scatter_autobow"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"bow",
		"silk_leather_string",
		"spring_box",
		"compound_wood"
	]
}
recipes["advanced_assembler"]["semi_frame"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"dense_alloy_sheet"
	] * 3 + ["standard_vehicle_chassis"]
}
recipes["advanced_assembler"]["shower_head"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"standard_pipes",
		"dense_mesh"
	]
}
recipes["advanced_assembler"]["sink"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"standard_pipes",
		"dense_mesh",
		"cauldron"
	]
}
recipes["advanced_assembler"]["solar_panel"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_generator_scrap",
		"industrial_scrap"
	] * 4
}
recipes["advanced_assembler"]["standard_assembler"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["advanced_assembler"]["standard_autobow"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"bow",
		"silk_leather_string",
		"metal_spring",
		"compound_wood"
	]
}
recipes["advanced_assembler"]["standard_vehicle_chassis"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"moldable_alloy_frame",
		"dense_alloy_sheet"
	]
}
recipes["advanced_assembler"]["steam_generator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_generator_scrap",
		"industrial_generator_scrap",
		"industrial_scrap"
	] * 8
}
recipes["advanced_assembler"]["truck_frame"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"standard_vehicle_chassis",
		"dense_alloy_sheet",
		"sheet_metal"
	]
}
recipes["advanced_assembler"]["vehicle_alternator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"simple_mechanism",
		"small_moldable_case",
		"conductive_fibers"
	]
}
recipes["advanced_assembler"]["vehicle_battery"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"dense_alloy_sheet",
		"conductive_fibers"
	]
}
recipes["advanced_assembler"]["vehicle_engine"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"moldable_alloy_frame",
		"dense_alloy_sheet",
		"metal_cylinder"
	]
}
recipes["advanced_assembler"]["vehicle_exhaust"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"iron_block"
	]
}
recipes["advanced_assembler"]["vehicle_frame"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"sheet_metal"
	] * 2
}
recipes["advanced_assembler"]["vehicle_fuel_tank"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"dense_alloy_sheet",
		"standard_moldable_case"
	]
}
recipes["advanced_assembler"]["vehicle_radiator"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"conductive_mesh"
	]
}
recipes["advanced_assembler"]["vehicle_trunk"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"moldable_alloy_frame",
		"dense_alloy_sheet",
		"chest"
	]
}
recipes["advanced_assembler"]["washer"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"iron_block",
		"moldable_alloy_frame",
		"metal_spring"
	]
}
recipes["advanced_assembler"]["wind_turbine"] = {
	"machine":"advanced_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 16 + ( ["industrial_generator_scrap"] * 4)
}
#Standard Assembler Recipes
recipes["standard_assembler"]["3_step_lock"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"3_step_dial",
		"tumbler",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["4_step_lock"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"4_step_dial",
		"tumbler",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["5_step_lock"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"5_step_dial",
		"tumbler",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["6_step_lock"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"6_step_dial",
		"tumbler",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["7_step_lock"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"7_step_dial",
		"tumbler",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["advanced_assembler"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["standard_assembler"]["advanced_house_alarm"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"block_alarm_detector",
		"chest_alarm_detector",
		"door_alarm_detector"
	] * 6 + ["small_moldable_case"]
}
recipes["standard_assembler"]["basic_assembler "] = {
	"machine":"standard_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["standard_assembler"]["basic_house_alarm"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"block_alarm_detector",
		"chest_alarm_detector",
		"door_alarm_detector",
		"small_moldable_case"
	]
}
recipes["standard_assembler"]["battery_jumper"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"battery_unit",
		"simple_mechanism"
	]
}
recipes["standard_assembler"]["battery_unit"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"sulfuric_acid",
		"metalic_rod"
	]
}
recipes["standard_assembler"]["chemical_assembler"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 32
}
recipes["standard_assembler"]["comfort_bed_6"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"metal_spring"
	]
}
recipes["standard_assembler"]["comfort_bed_7"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"cotton_wool",
		"metal_spring"
	]
}
recipes["standard_assembler"]["comfort_bed_8"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"metal_spring",
		"metal_spring"
	]
}
recipes["standard_assembler"]["compound_wood"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"dense_mesh",
		"metalic_rod",
		"wood"
	]
}
recipes["standard_assembler"]["conductive_fibers"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"redstone",
		"metalic_fiber"
	]
}
recipes["standard_assembler"]["conductive_glass"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"glass_crystals",
		"conductive_mesh"
	]
}
recipes["standard_assembler"]["conductive_mesh"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"simple_mesh",
		"conductive_fibers"
	]
}
recipes["standard_assembler"]["dense_fiber"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"metalic_fiber",
		"dense_alloy_bar"
	]
}
recipes["standard_assembler"]["dense_mesh"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"simple_mesh",
		"dense_fiber"
	]
}
recipes["standard_assembler"]["fire_extinguisher"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"small_moldable_case",
		"simple_mechanism",
		"thermal_insulator"
	]
}
recipes["standard_assembler"]["freezer"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"standard_moldable_case",
		"battery_unit",
		"conductive_mesh",
		"conductive_mesh"
	]
}
recipes["standard_assembler"]["item_brander"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 32
}
recipes["standard_assembler"]["jumper_cables"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"rubber",
		"metalic_rod",
		"conductive_fibers"
	]
}
recipes["standard_assembler"]["large_garage_door"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"moldable_alloy_frame"
	] * 3 + ["simple_mechanism"]
}
recipes["standard_assembler"]["lawn_mower"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"metal_blades",
		"moldable_alloy_frame"
	]
}
recipes["standard_assembler"]["medium_garage_door"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"moldable_alloy_frame"
	] * 2 + ["simple_mechanism"]
}
recipes["standard_assembler"]["organic_shell"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"sap",
		"plant_fiber"
	]
}
recipes["standard_assembler"]["refrigerator"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"standard_moldable_case",
		"battery_unit",
		"conductive_mesh"
	]
}
recipes["standard_assembler"]["sensor"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"metalic_rod",
		"battery_unit"
	]
}
recipes["standard_assembler"]["silk_leather_string"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"silk_leather",
		"string"
	]
}
recipes["standard_assembler"]["silk_leather"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"silk_strands",
		"leather_strands"
	]
}
recipes["standard_assembler"]["small_garage_door"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"simple_mechanism",
		"moldable_alloy_frame"
	]
}
recipes["standard_assembler"]["spring_box"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"metal_spring"
	] * 3
}
recipes["standard_assembler"]["standard_assembler"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["standard_assembler"]["standard_house_alarm"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"block_alarm_detector",
		"chest_alarm_detector",
		"door_alarm_detector"
	] * 3 + ["small_moldable_case"]
}
recipes["standard_assembler"]["standard_pipes"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"metalic_rod",
		"simple_alloy_bar"
	]
}
recipes["standard_assembler"]["standard_pump"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"sensor",
		"standard_pipes"
	]
}
recipes["standard_assembler"]["thermal_insulator"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"small_moldable_case",
		"fiber_glass"
	]
}
recipes["standard_assembler"]["vehicle_tire"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"rubber",
		"metal_cylinder"
	]
}
recipes["standard_assembler"]["null"] = {
	"machine":"standard_assembler",
	"ingredients": [
		"simple_mesh"
	]
}
#Basic Assembler Recipes
recipes["basic_assembler"]["acacia_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"yellow_dye"
	]
}
recipes["basic_assembler"]["basic_assembler"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["basic_assembler"]["battery"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["basic_assembler"]["birch_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"white_dye"
	]
}
recipes["basic_assembler"]["block_alarm_detector"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sensor",
		"battery_unit"
	]
}
recipes["basic_assembler"]["chest_alarm_detector"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sensor",
		"battery_unit"
	]
}
recipes["basic_assembler"]["comfort_bed_1"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bed",
		"wool_fibers"
	]
}
recipes["basic_assembler"]["comfort_bed_2"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bed",
		"wool_fibers",
		"wool_fibers"
	]
}
recipes["basic_assembler"]["comfort_bed_3"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"wool_fibers"
	]
}
recipes["basic_assembler"]["comfort_bed_4"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"wool_fibers",
		"wool_fibers"
	]
}
recipes["basic_assembler"]["comfort_bed_5"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bed",
		"cotton_wool",
		"cotton_wool"
	]
}
recipes["basic_assembler"]["cooler"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"chest",
		"thermal_insulator"
	]
}
recipes["basic_assembler"]["coordinator"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["basic_assembler"]["cotton_wool"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"wool",
		"wool_fibers"
	]
}
recipes["basic_assembler"]["water_barrel"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"bucket"
	] * 3
}
recipes["basic_assembler"]["water_crate"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"water_barrel"
	] * 3
}
recipes["basic_assembler"]["dark_oak_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"brown_dye"
	]
}
recipes["basic_assembler"]["dehumidifier"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 4
}
recipes["basic_assembler"]["dense_rubber"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"rubber"
	] * 2
}
recipes["basic_assembler"]["door_alarm_detector"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sensor",
		"battery_unit"
	]
}
recipes["basic_assembler"]["extractor"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 4
}
recipes["basic_assembler"]["fire_foam"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sponge"
	]
}
recipes["basic_assembler"]["jerry_can"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"small_moldable_case",
		"sheet_metal"
	]
}
recipes["basic_assembler"]["jungle_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"orange_dye"
	]
}
recipes["basic_assembler"]["key_copy_kit"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"clay_ball",
		"small_moldable_case"
	]
}
recipes["basic_assembler"]["leather_strands"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"leather",
		"wool"
	]
}
recipes["basic_assembler"]["mechanics_wrench"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sheet_metal",
		"metalic_rod"
	]
}
recipes["basic_assembler"]["melter"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 4
}
recipes["basic_assembler"]["metal_caster"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 8
}
recipes["basic_assembler"]["metalic_fiber"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"plant_fiber",
		"iron_fragments"
	]
}
recipes["basic_assembler"]["mover"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 4
}
recipes["basic_assembler"]["oak_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"silver_dye"
	]
}
recipes["basic_assembler"]["rubber"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"simple_mesh"
	]
}
recipes["basic_assembler"]["silk_strands"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"web",
		"wool"
	]
}
recipes["basic_assembler"]["simple_backpack"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"leather"
	] * 5 + ["string","string"]
}
recipes["basic_assembler"]["simple_mechanism"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"metalic_rod",
		"simple_alloy_bar"
	]
}
recipes["basic_assembler"]["simple_mesh"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"metalic_fiber"
	] * 2
}
recipes["basic_assembler"]["small_rotor"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"metalic_rod"
	]
}
recipes["basic_assembler"]["smeltry"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 8
}
recipes["basic_assembler"]["spacious_backpack"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"leather"
	] * 20 + (["string"] * 8) + ["simple_mesh","simple_mesh"]
}
recipes["basic_assembler"]["split_water_barrel"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"full_water_barrel"
	]
}
recipes["basic_assembler"]["split_water_crate"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"full_water_crate"
	]
}
recipes["basic_assembler"]["spruce_car_paint"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"sap",
		"brown_dye"
	]
}
recipes["basic_assembler"]["standard_assembler"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"industrial_scrap"
	] * 10
}
recipes["basic_assembler"]["thick_backpack"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"leather"
	] * 10 + (["string"] * 4) + ["simple_mesh"]
}
recipes["basic_assembler"]["tire_mesh"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"rubber",
		"simple_mesh"
	]
}
recipes["basic_assembler"]["wool_fibers"] = {
	"machine":"basic_assembler",
	"ingredients": [
		"wool"
	]
}
#Dehumidifier recipes
recipes["dehumidifier"]["water_bucket"] = {
	"machine":"dehumidifier",
	"ingredients": [
		"bucket",
		"sponge"
	]
}
#Component Manipulator Recipes
recipes["component_manipulator"]["4_cylinder_engine"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"metal_cylinder",
		"sheet_metal"
	]
}
recipes["component_manipulator"]["6_cylinder_engine"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"metal_cylinder",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["8_cylinder_engine"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"metal_cylinder",
		"dense_alloy_sheet",
		"conductive_mesh"
	]
}
recipes["component_manipulator"]["conductive_radiator"] = {
	"machine":"component_manipulator",
	"base": "vehicle_radiator",
	"ingredients": [
		"conductive_mesh"
	]
}
recipes["component_manipulator"]["converter_efficiency"] = {
	"machine":"component_manipulator",
	"base": "unknown",
	"ingredients": [
		"sensor",
		"simple_mechanism"
	]
}
recipes["component_manipulator"]["dense_engine_block"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["double_exhaust"] = {
	"machine":"component_manipulator",
	"base": "vehicle_exhaust",
	"ingredients": [
		"standard_pipes",
		"sheet_metal"
	]
}
recipes["component_manipulator"]["engine_efficient_cylinders"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"metal_cylinder",
		"sensor"
	]
}
recipes["component_manipulator"]["expanded_fuel_tank"] = {
	"machine":"component_manipulator",
	"base": "vehicle_fuel_tank",
	"ingredients": [
		"dense_mesh",
		"standard_moldable_case"
	]
}
recipes["component_manipulator"]["expanded_trunk"] = {
	"machine":"component_manipulator",
	"base": "vehicle_trunk",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet",
		"standard_moldable_case"
	]
}
recipes["component_manipulator"]["extra_compartments"] = {
	"machine":"component_manipulator",
	"base": "vehicle_trunk",
	"ingredients": [
		"dense_alloy_sheet",
		"small_moldable_case"
	]
}
recipes["component_manipulator"]["extra_fuel_tank"] = {
	"machine":"component_manipulator",
	"base": "vehicle_fuel_tank",
	"ingredients": [
		"moldable_alloy_frame",
		"standard_moldable_case"
	]
}
recipes["component_manipulator"]["heavy_frame"] = {
	"machine":"component_manipulator",
	"base": "vehicle_frame",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["internal_cooler"] = {
	"machine":"component_manipulator",
	"base": "vehicle_radiator",
	"ingredients": [
		"dense_alloy_sheet",
		"thermal_insulator"
	]
}
recipes["component_manipulator"]["light_frame"] = {
	"machine":"component_manipulator",
	"base": "vehicle_frame",
	"ingredients": [
		"sheet_metal",
		"metalic_fiber"
	]
}
recipes["component_manipulator"]["noncorrosive_exhaust"] = {
	"machine":"component_manipulator",
	"base": "vehicle_exhaust",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["noncorrosive_frame"] = {
	"machine":"component_manipulator",
	"base": "vehicle_frame",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["offroad_treads"] = {
	"machine":"component_manipulator",
	"base": "vehicle_tire",
	"ingredients": [
		"tire_mesh",
		"dense_rubber"
	]
}
recipes["component_manipulator"]["reinforced_engine_block"] = {
	"machine":"component_manipulator",
	"base": "vehicle_engine",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["reinforced_frame"] = {
	"machine":"component_manipulator",
	"base": "vehicle_frame",
	"ingredients": [
		"simple_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["reinforced_fuel_tank"] = {
	"machine":"component_manipulator",
	"base": "vehicle_fuel_tank",
	"ingredients": [
		"dense_mesh",
		"dense_alloy_sheet"
	]
}
recipes["component_manipulator"]["secondary_starter_fuse"] = {
	"machine":"component_manipulator",
	"base": "vehicle_battery",
	"ingredients": [
		"simple_mechanism",
		"sheet_metal"
	]
}
recipes["component_manipulator"]["thick_radiator"] = {
	"machine":"component_manipulator",
	"base": "vehicle_radiator",
	"ingredients": [
		"dense_alloy_sheet",
		"dense_mesh"
	]
}
recipes["component_manipulator"]["thick_treads"] = {
	"machine":"component_manipulator",
	"base": "vehicle_tire",
	"ingredients": [
		"tire_mesh",
		"dense_rubber"
	]
}
recipes["component_manipulator"]["thin_treads"] = {
	"machine":"component_manipulator",
	"base": "vehicle_tire",
	"ingredients": [
		"tire_mesh",
		"rubber"
	]
}
recipes["component_manipulator"]["winter_treads"] = {
	"machine":"component_manipulator",
	"base": "vehicle_tire",
	"ingredients": [
		"tire_mesh",
		"thermal_insulator"
	]
}
#Smeltry Recipes
recipes["smeltry"]["dense_alloy_bar"] = {
	"machine":"smeltry",
	"ingredients": [
		"gold_fragments",
		"iron_fragments"
	] * 2
}
recipes["smeltry"]["simple_alloy_bar"] = {
	"machine":"smeltry",
	"ingredients": [
		"gold_fragments",
		"iron_fragments"
	]
}
#Chemical Assembler Recipes
recipes["chemical_assembler"]["antibiotic_a"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"organic_shell",
		"organic_ferment",
		"red_bacteria"
	]
}
recipes["chemical_assembler"]["antibiotic_b"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"organic_shell",
		"robust_cells",
		"brown_bacteria"
	]
}
recipes["chemical_assembler"]["antibiotic_c"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"organic_shell",
		"lactobacillus",
		"organic_ferment"
	]
}
recipes["chemical_assembler"]["antibiotic_d"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"organic_shell",
		"robust_cells",
		"red_bacteria"
	]
}
recipes["chemical_assembler"]["brown_bacteria"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"brown_mushroom"
	]
}
recipes["chemical_assembler"]["glass_crystals"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"glass"
	]
}
recipes["chemical_assembler"]["glass_vial"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"glass_bottle"
	]
}
recipes["chemical_assembler"]["glowstone_crystals"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"glowstone_dust",
		"ice"
	]
}
recipes["chemical_assembler"]["lactobacillus"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"milk_bucket"
	]
}
recipes["chemical_assembler"]["organic_ferment"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"egg"
	]
}
recipes["chemical_assembler"]["polymer_silk_leather"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"silk_leather",
		"string",
		"plant_fiber"
	]
}
recipes["chemical_assembler"]["red_bacteria"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"red_mushroom"
	]
}
recipes["chemical_assembler"]["robust_cells"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"spider_eye"
	]
}
recipes["chemical_assembler"]["sulfur"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"coal",
		"glowstone_crystals"
	]
}
recipes["chemical_assembler"]["sulfuric_acid"] = {
	"machine":"chemical_assembler",
	"ingredients": [
		"sulfur"
	]
}
#Metal Caster Recipes
recipes["metal_caster"]["3_step_dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"dial"
	] * 3
}
recipes["metal_caster"]["4_step_dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"dial",
		"3_step_dial"
	]
}
recipes["metal_caster"]["5_step_dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"dial",
		"dial",
	] * 2 + ["3_step_dial"]
}
recipes["metal_caster"]["6_step_dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"3_step_dial"
	] * 2
}
recipes["metal_caster"]["7_step_dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"3_step_dial",
		"dial"
	]
}
recipes["metal_caster"]["dense_alloy_sheet"] = {
	"machine":"metal_caster",
	"ingredients": [
		"dense_alloy_bar"
	]
}
recipes["metal_caster"]["dial"] = {
	"machine":"metal_caster",
	"ingredients": [
		"simple_alloy_bar"
	]
}
recipes["metal_caster"]["metal_blades"] = {
	"machine":"metal_caster",
	"ingredients": [
		"sheet_metal",
		"metalic_rod"
	]
}
recipes["metal_caster"]["metal_cylinder"] = {
	"machine":"metal_caster",
	"ingredients": [
		"iron_fragments"
	]
}
recipes["metal_caster"]["metal_spring"] = {
	"machine":"metal_caster",
	"ingredients": [
		"iron_fragments"
	]
}
recipes["metal_caster"]["metalic_rod"] = {
	"machine":"metal_caster",
	"ingredients": [
		"simple_alloy_bar"
	]
}
recipes["metal_caster"]["moldable_alloy_frame"] = {
	"machine":"metal_caster",
	"ingredients": [
		"sheet_metal",
		"metalic_rod"
	]
}
recipes["metal_caster"]["sheet_metal"] = {
	"machine":"metal_caster",
	"ingredients": [
		"simple_alloy_bar"
	]
}
recipes["metal_caster"]["small_moldable_case"] = {
	"machine":"metal_caster",
	"ingredients": [
		"simple_alloy_bar"
	]
}
recipes["metal_caster"]["standard_moldable_case"] = {
	"machine":"metal_caster",
	"ingredients": [
		"simple_alloy_bar"
	] * 2
}
recipes["metal_caster"]["tumbler"] = {
	"machine":"metal_caster",
	"ingredients": [
		"gold_fragments"
	]
}
#Extractor Recipes
recipes["extractor"]["gold_fragments"] = {
	"machine":"extractor",
	"ingredients": [
		"gold_ore"
	]
}
recipes["extractor"]["iron_fragments"] = {
	"machine":"extractor",
	"ingredients": [
		"iron_ore"
	]
}
recipes["extractor"]["plant_fiber"] = {
	"machine":"extractor",
	"ingredients": [
		["red_rose"],
		["wheat"],
		["sugar_cane"],
		["yellow_flower"]
	]
}
recipes["extractor"]["sap"] = {
	"machine":"extractor",
	"ingredients": [
		["log_2"],
		["sapling"]*4,
		["log"]
	]
}
#Functions
def get_recipe(item, machine=False):
	if machine:
		if item in recipes[machine]:
			return recipes[machine][item]
		else:
			return False
	else:
		for machine in recipes:
			if item in recipes[machine]:
				return recipes[machine][item]
	return False

def add_recipe(machine, item, ingredients):
	recipes[machine][item] = {
		"machine":machine,
		"ingredients": ingredients
	}
	return recipes[machine][item]

def add_machine(machine):
	recipes[machine] = {}
	return recipes[machine]

def index_recipes():
	global indexes
	indexes = {}
	for machine in recipes:
		for item in recipes[machine]:
			if not item in indexes:
				if type(recipes[machine][item]["ingredients"][0]) == list:
					ingredients = recipes[machine][item]["ingredients"][0]
				else:
					ingredients = recipes[machine][item]["ingredients"]
				highest_index = 0
				for ingredient in ingredients:
					cur_index = index_item(ingredient)
					if cur_index > highest_index:
						highest_index = cur_index
				indexes[item] = highest_index + 1

def index_item(item):
	if not item in indexes:
		for machine in recipes:
			if item in recipes[machine]:
				if type(recipes[machine][item]["ingredients"][0]) == list:
					ingredients = recipes[machine][item]["ingredients"][0]
				else:
					ingredients = recipes[machine][item]["ingredients"]
				highest_index = 0
				for ingredient in ingredients:
					cur_index = index_item(ingredient)
					if cur_index > highest_index:
						highest_index = cur_index
				indexes[item] = highest_index + 1
				return highest_index + 1
		indexes[item] = 0
		return 0
	else:
		return indexes[item]

def calculate_cost(item, costs={}, level=0):
	for machine in recipes:
		if item in recipes[machine]:
			recipe = recipes[machine][item]["ingredients"]
			if type(recipe[0]) == list:
				recipe = recipe[0]
			for ingredient in recipe:
				try:
					pass
				except KeyError:
					print("err: " + ingredient)
					print(recipe)
					print("index: " + indexes[ingredient])
				calculate_cost(ingredient, costs, level+1)
			if not indexes[item] in costs:
				costs[indexes[item]] = {}
			if not item in costs[indexes[item]]:
				costs[indexes[item]][item] = 1
			else:
				costs[indexes[item]][item] += 1
			return costs
	if not 0 in costs:
		costs[0] = {}
	if not item in costs[0]:
		costs[0][item] = 1
	else:
		costs[0][item] += 1
	return True
index_recipes()