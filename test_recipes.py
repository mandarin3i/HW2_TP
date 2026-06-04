import pytest
from Ingrediens import Ingredient
from ShoppingList import ShoppingList
from recipe import Recipe
#1
def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"
def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"
def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 300.0, "г")
    ing3 = Ingredient("Сахар", 500.0, "г")
    ing4 = Ingredient("Мука", 500.0, "кг")
    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4

#2
def test_shopping_list_add_recipe():
    sl = ShoppingList()
    recipe = Recipe("Тесто", [Ingredient("Мука", 200.0, "г")])
    sl.add_recipe(recipe, 2)
    assert len(sl._items) == 1
    with pytest.raises(ValueError):
        sl.add_recipe(recipe,-1)
def test_shopping_list_remove_recipe():
    sl = ShoppingList()
    recipe1 = Recipe("Тесто", [Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Крем", [Ingredient("Сахар", 100.0, "г")])  
    sl.add_recipe(recipe1, 1)
    sl.add_recipe(recipe2, 1)
    sl.remove_recipe("Тесто")  
    assert len(sl._items) == 1
    assert sl._items[0][1] == "Крем"

def test_shopping_list_get_list():
    sl = ShoppingList()
    recipe1 = Recipe("Тесто", [Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Блины", [Ingredient("Мука", 300.0, "г"), Ingredient("Вода", 100.0, "мл")]) 
    sl.add_recipe(recipe1, 1)
    sl.add_recipe(recipe2, 1)  
    final_list = sl.get_list()
    assert len(final_list) == 2
    assert final_list[0].name == "Вода"
    assert final_list[0].quantity == 100.0
    assert final_list[1].name == "Мука"
    assert final_list[1].quantity == 500.0

def test_shopping_list_add_operator():
    sl1 = ShoppingList()
    sl1.add_recipe(Recipe("А", [Ingredient("Соль", 10.0, "г")]), 1) 
    sl2 = ShoppingList()
    sl2.add_recipe(Recipe("Б", [Ingredient("Сахар", 20.0, "г")]), 1)
    sl3 = sl1+sl2
    assert len(sl3._items) == 2
    assert len(sl1._items) == 1
    assert len(sl2._items) == 1

#3
def test_recipe_creation():
    ing1 = Ingredient("Мука", 500.0, "г")
    recipe = Recipe("Пицца", [ing1])
    assert recipe.title == "Пицца"
    assert len(recipe) == 1
def test_recipe_add_ingredient():
    recipe = Recipe("Торт")
    recipe.add_ingredient(Ingredient("Яйцо", 2.0, "шт"))
    recipe.add_ingredient(Ingredient("Яйцо", 3.0, "шт"))    
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 5.0
def test_recipe_scale():
    recipe = Recipe("Тесто", [Ingredient("Мука", 200.0, "г")])
    scaled = recipe.scale(2.5)    
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity == 500.0
    assert recipe.ingredients[0].quantity == 200.0 
    with pytest.raises(ValueError):
        recipe.scale(0)
def test_recipe_len():
    recipe = Recipe("Пицца", [Ingredient("Мука", 200.0, "г"), Ingredient("Вода", 100.0, "мл")])
    assert len(recipe) == 2
