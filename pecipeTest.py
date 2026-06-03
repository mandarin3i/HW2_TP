import pytest
from recipe import Recipe

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
