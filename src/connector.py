import json
from src.mongodb_token import uri
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Connector:
    # Basic settings
    working_directory = os.path.dirname(__file__)
    dishes_file_path = os.path.join(
        working_directory, 'data', 'dishes.json')
    ingredients_file_path = os.path.join(
        working_directory, 'data', 'ingredients.json')
    config_file_path = os.path.join(
        working_directory, 'data', 'config.json')
    client = MongoClient(uri, server_api=ServerApi('1'))
    database = client["Bity_smarty"]
    dishes_collection = database["dishes"]
    ingredients_collection = database["ingredients"]
    config_collection = database["config"]

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
    def get_dishes(self):
        if self.data_source == 'json':
            return Connector.read_json_file(Connector.dishes_file_path)
        return Connector.dishes_collection.find_one()

    # Get ingredients list
    def get_ingredients(self):
        if self.data_source == 'json':
            return Connector.read_json_file(Connector.ingredients_file_path)
        return Connector.ingredients_collection.find_one()

    # Get config
    def get_config(self):
        if self.data_source == 'json':
            return Connector.read_json_file(Connector.config_file_path)
        elif self.data_source == 'mongodb':
            return Connector.config_collection.find_one()

    # Set config
    def set_config(self, data):
        if self.data_source == 'json':
            return Connector.write_json_file(Connector.config_file_path, data)
        elif self.data_source == 'mongodb':
            Connector.config_collection.delete_many({})
            Connector.config_collection.insert_one(data)
