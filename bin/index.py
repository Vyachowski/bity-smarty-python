from functions import getCurrentTime, hasPassedGivenDays, mergeAndSumObjects, multiplyObjectValues, objectToTextColumn
from connector import Connector

class Diet:
    def __init__(self):
      self._connector = Connector()
      self._dishes = self._connector.get_dishes()
      self._ingredients = self._connector.get_ingredients()
      self._config = self._connector.get_config()
      self._menu_duration = 3

    @staticmethod
    def get_random_meal(meal_variants):
        import random
        if meal_variants:
            meal = random.choice(meal_variants)
            name = meal.get('name', '')
            portions = meal.get('portions', 1)
            ingredients = meal.get('ingredients', meal)
            return {'name': name, 'portions': portions, 'ingredients': ingredients}
        return None

    def _create_random_menu(self):
        return {
        'breakfast': Diet.get_random_meal(self._dishes['breakfast']),
        'snack': Diet.get_random_meal(self._dishes['snack']),
        'lunch': Diet.get_random_meal(self._dishes['lunch']),
        'dinner': Diet.get_random_meal(self._dishes['dinner']),
        }

    def _create_ingredients_list(self):
        all_ingredients = mergeAndSumObjects(*[meal['ingredients'] for meal in self._config['menu'].values() if meal])
        ingredients_list = multiplyObjectValues(all_ingredients, self._menu_duration)
        return ingredients_list

    def _create_grocery_list(self):
        all_ingredients_list = self._ingredients.items()
        ingredients_list = self._config.get('ingredientsList', {})
        sections = set(prop['section'] for _, prop in all_ingredients_list)

        ingredients_by_section = []
        for section in sections:
            products = [product for product, prop in all_ingredients_list if prop.get('section') == section]
            ingredients_by_section.append({'section': section, 'products': products})

        grocery_list = []
        for item in ingredients_by_section:
            section = item['section']
            products = item['products']
            product_amount = [{product: ingredients_list.get(product, 0)} for product in products if ingredients_list.get(product) is not None]
            grocery_list.append({'section': section, 'productAmount': product_amount})

        return grocery_list

    def _set_ingredients_list(self):
        self._config['ingredientsList'] = self._create_ingredients_list()
        self._connector.set_config(self._config)

    def set_menu(self):
        if not hasPassedGivenDays(self._config.get('date'), self._menu_duration):
            print("Menu is still up-to-date")
            return

        try:
            self._config['date'] = getCurrentTime()
            self._config['menu'] = self._create_random_menu()
            self._connector.set_config(self._config)
        except Exception as error:
            print("Error while setting the menu:", error)
        else:
            print("Menu successfully created")

    def set_grocery_list(self):
        try:
            self._config['ingredientsList'] = self._create_ingredients_list()
            self._config['groceryList'] = self._create_grocery_list()
            self._connector.set_config(self._config)
        except Exception as error:
            print("Error while setting the grocery list:", error)
        else:
            print("Grocery list successfully set")

    def get_menu(self):
        menu = {
        'For breakfast · 🥓 · 🧇 · 🥞 · 🍳': self._config['menu']['breakfast'],
        'For snack · 🍎 · 🍪 · 🥨 · 🍫 · ': self._config['menu']['snack'],
        'For lunch · 🍽️ · 🥪 · 🍱 · 😋 ': self._config['menu']['lunch'],
        'For dinner · 🥘 · 🍲 · 🥣 · 🥗 ': self._config['menu']['dinner'],
        }

        current_menu_array = [
        f"| {meal_name}\n| {dish['name'].upper()}\n\n{objectToTextColumn(dish['ingredients'])}\n\n"
        for meal_name, dish in menu.items() if dish
        ]
        current_menu = ''.join(current_menu_array)
        return current_menu

    def get_grocery_list(self):
        grocery_list_array = self._config.get('groceryList', [])
        grocery_list_columns = [
            f"| {section['section'].upper()}\n\n{'' if not section['productAmount'] else '\n'.join([objectToTextColumn(product) for product in section['productAmount']])}\n\n"
            for section in grocery_list_array
        ]
        grocery_list = ''.join(grocery_list_columns)
        return grocery_list

    def display_menu(self):
        menu = {
            'For breakfast · 🥓 · 🧇 · 🥞 · 🍳': self._config['menu']['breakfast'],
            'For snack · 🍎 · 🍪 · 🥨 · 🍫 · ': self._config['menu']['snack'],
            'For lunch · 🍽️ · 🥪 · 🍱 · 😋 ': self._config['menu']['lunch'],
            'For dinner · 🥘 · 🍲 · 🥣 · 🥗 ': self._config['menu']['dinner'],
        }

        for meal_name, dish in menu.items():
            if dish:
                print(f"| {meal_name}\n| {dish['name'].upper()}\n\n{objectToTextColumn(dish['ingredients'])}\n")

    def display_grocery_list(self):
        grocery_list_array = self._config.get('groceryList', [])
        for section in grocery_list_array:
            print(f"| {section['section'].upper()}\n\n{'' if not section['productAmount'] else '\n'.join([objectToTextColumn(product) for product in section['productAmount']])}\n")

    # if __name__ == "__main__":
    #     diet = Diet()
    #     diet.set_menu()
    #     diet.set_grocery_list()
    #     diet.display_menu()
    #     diet.display_grocery_list()
