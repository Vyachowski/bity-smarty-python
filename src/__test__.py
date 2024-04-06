from src.connector import Connector
from src.main import Diet

# TESTS
connect = Connector()  # // Passed
print(connect.working_directory)  # // Passed
print(connect.dishes_file_path)  # // Passed
print(connect.ingredients_file_path)  # // Passed
print(connect.config_file_path)  # // Passed
print(connect.client)  # // Passed
print(connect.database)  # // Passed
print(connect.dishes_collection)  # // Passed
print(connect.ingredients_collection)  # // Passed
print(connect.config_collection)  # // Passed
print(connect.get_config())  # // Passed
print(connect.get_dishes())  # // Passed
print(connect.get_ingredients())  # // Passed


diet = Diet()  # // Passed
print(diet._create_ingredients_list())  # // Passed
print(diet._set_ingredients_list())  # // Passed
print(diet._create_grocery_list())  # // Passed
print(diet.set_grocery_list())  # // Passed
print(diet.get_dishes_list())  # // Passed
diet.display_dishes_list()  # // Passed
