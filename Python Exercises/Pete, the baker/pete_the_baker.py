def cakes(recipe: dict, available:dict) -> int:
    recipe_ingredients = set(recipe.keys())
    available_ingredients = set(available.keys())

    cakes_to_bake:int = 0
    
    if recipe_ingredients.issubset(available_ingredients):
        
        
        
                
    else: return 0
    
if __name__ == "__main__":
    print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))