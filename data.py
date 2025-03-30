class Ingredient:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class Dish:
    def __init__(self, name: str, ingredients: [Ingredient]):
        self.name = name
        self.ingredients = ingredients

    def get_name(self) -> str:
        return self.name
    def get_ingredients(self) -> [Ingredient]:
        return self.ingredients