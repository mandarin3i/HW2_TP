class ShoppingList:
    def __init__(self):
        self._items = []  
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, recipe.title))
          
    def remove_recipe(self, title: str):
        self._items=[item for item in self._items if item[1]!=title]

    def get_list(self):
        agg = {}
        for ing, _ in self._items:
            key = (ing.name, ing.unit)
            if key in agg:
                agg[key]+=ing.quantity
            else:
                agg[key] = ing.quantity     
        result = [Ingredient(name, qty, unit) for (name, unit), qty in agg.items()]
        result.sort(key=lambda x: x.name) #в чате лямбда функции разрешили
        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list
