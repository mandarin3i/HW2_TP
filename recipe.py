class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title=title
        self.ingredients = []
        if ingredients:
            for ing in ingredients:
                self.add_ingredient(ing)
    def add_ingredient(self, ingredient: Ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity+=ingredient.quantity
                return
        self.ingredients.append(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Ratio должно быть положительным числом")      
        scaled_ingredients = [Ingredient(ing.name, ing.quantity * ratio, ing.unit) for ing in self.ingredients]
        return Recipe(self.title, scaled_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        ings_str = "\n".join(f" - {ing}" for ing in self.ingredients)
        return f"Рецепт: {self.title}\nИнгредиенты:\n{ings_str}"
