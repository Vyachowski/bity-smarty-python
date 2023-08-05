import json
import os


class Connector:
    # Basic settings
    working_directory = os.getcwd()
    dishes_file_path = os.path.join(
        working_directory, 'src', 'data', 'dishes.json')
    ingredients_file_path = os.path.join(
        working_directory, 'src', 'data', 'ingredients.json')
    config_file_path = os.path.join(
        working_directory, 'src', 'data', 'config.json')

    # Selecting a data source
    def __init__(self, data_source='json'):
        self.data_source = data_source

    # Read a JSON file
    @staticmethod
    def read_json_file(file_path):
        try:
            with open(file_path, 'r') as file:
                json_object = json.load(file)
            return json_object
        except Exception as error:
            print('Error reading file or converting JSON:', error)
            raise error

    # Write a JSON file
    @staticmethod
    def write_json_file(file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
        except Exception as error:
            print('Error writing file:', error)
            raise error

    # Get dishes list
    @staticmethod
    def get_dishes():
        return Connector.read_json_file(Connector.dishes_file_path)

    # Get ingredients list
    @staticmethod
    def get_ingredients():
        return Connector.read_json_file(Connector.ingredients_file_path)

    # Get config
    @staticmethod
    def get_config():
        return Connector.read_json_file(Connector.config_file_path)

    # Set config
    @staticmethod
    def set_config(data):
        Connector.write_json_file(Connector.config_file_path, data)
