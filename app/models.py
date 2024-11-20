class MealItem:
    def __init__(self, nutrition_dict):
        self.calcium = float(nutrition_dict.get("calcium", 0))
        self.calories = float(nutrition_dict.get("calories", 0))
        self.cholesterol = float(nutrition_dict.get("cholesterol", 0))
        self.dietary_fiber = float(nutrition_dict.get("dietaryFiber", 0))
        self.iron = float(nutrition_dict.get("iron", 0))
        self.is_eat_well = nutrition_dict.get("isEatWell", False)
        self.is_plant_forward = nutrition_dict.get("isPlantForward", False)
        self.is_vegan = nutrition_dict.get("isVegan", False)
        self.is_vegetarian = nutrition_dict.get("isVegetarian", False)
        self.is_whole_grain = nutrition_dict.get("isWholeGrain", False)
        self.protein = float(nutrition_dict.get("protein", 0))
        self.saturated_fat = float(nutrition_dict.get("saturatedFat", 0))
        self.serving_size = float(nutrition_dict.get("servingSize", 0))
        self.serving_unit = nutrition_dict.get("servingUnit", "")
        self.sodium = float(nutrition_dict.get("sodium", 0))
        self.sugars = float(nutrition_dict.get("sugars", 0))
        self.total_carbohydrates = float(nutrition_dict.get("totalCarbohydrates", 0))
        self.total_fat = float(nutrition_dict.get("totalFat", 0))
        self.trans_fat = float(nutrition_dict.get("transFat", 0))
        self.vitamin_a = float(nutrition_dict.get("vitaminA", 0))
        self.vitamin_c = float(nutrition_dict.get("vitaminC", 0))

    def calculate_dri(self):
        # TODO: Implement this method
        return dri

