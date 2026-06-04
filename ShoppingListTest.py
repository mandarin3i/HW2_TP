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
