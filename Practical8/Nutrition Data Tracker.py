class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
def summarize_daily_intake(food_list):
    total_cal = 0
    total_prot = 0
    total_carb = 0
    total_fat = 0
    for item in food_list:
        total_cal += item.calories
        total_prot += item.protein
        total_carb += item.carbs
        total_fat += item.fat        
    print("--- 24-Hour Nutrition Report ---")
    print(f"Total Calories: {total_cal:.1f} kcal")
    print(f"Total Protein: {total_prot:.1f} g")
    print(f"Total Carbohydrates: {total_carb:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")
    if total_cal > 2500:
        print("WARNING: Calorie consumption exceeds 2,500 kcal!")
    if total_fat > 90:
        print("WARNING: Fat consumption exceeds 90 g!")
apple = food_item("Apple", 60, 0.3, 15, 0.5)
burger = food_item("Burger", 800, 30, 45, 50)
pizza = food_item("Pizza", 1800, 70, 200, 60)
my_meals = [apple, burger, pizza]
summarize_daily_intake(my_meals)