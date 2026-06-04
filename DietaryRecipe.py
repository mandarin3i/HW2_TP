class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float):
        scaled_base = super().scale(ratio)
        return DietaryRecipe(scaled_base.title, self.diet_type, scaled_base.ingredients)
    def __str__(self):
        base_str = super().__str__()
        return f"[{self.diet_type}] " + base_str.replace("Рецепт: ", "")
