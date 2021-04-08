from .api_settings import Settings

import requests


class StarWarsSearch:
    """ Star Wars Api Search class

    searches inside the swapi api.
    the class has two main functions:
    1) starwars_search
    2) get_function
    """
    def __init__(self):
        self.settings = Settings()
        self.response = None
        self.response_info = None
        self.output = []
        self.get_output = {}
        self.counter = 0

    def starwars_search(self, category, attribute, filters):
        """searches category by attribute result filtered by input parameter (category, attribute, filters)
        Args:
            category (str): string inputs must be (films, people, planets, species, starships, vehicles)
            attribute (str): string inputs depending of category input(name, title, birth_year, eye_color,
            gender, hair_color, height, mass, skin_color, homeworld, films, species, starships,
            vehicles, created, edited).
            filters (str): specific attribute you're searching for accepts any.
        """
        self.load_response(category)
        while self.counter != int(self.response_info['count']):
            self.attribute_search(attribute, filters)
            self.load_next_response()

    def attribute_search(self, attribute, filters):
        """searches if filters in attribute
        Args:
            attribute (str): string inputs depending of category input(name, title, birth_year, eye_color,
            gender, hair_color, height, mass, skin_color, homeworld, films, species, starships,
            vehicles, created, edited).
            filters (str): specific attribute you're searching for accepts any.
        """
        for i in self.response_info['results']:
            if filters in i[attribute]:
                self.output.append(i)
            self.counter += 1

    def get_function(self, category, attribute):
        """searches category's attribute's.
        Args:
            category (str): string inputs must be (films, people, planets, species, starships, vehicles)
            attribute (str): string inputs depending of category input(name, title, birth_year, eye_color,
            gender, hair_color, height, mass, skin_color, homeworld, films, species, starships,
            vehicles, created, edited).
        """
        self.load_response(category)
        while self.counter != int(self.response_info['count']):
            self.attribute_name_marge(attribute, category)
            self.load_next_response()

    def attribute_name_marge(self, attribute, category):
        """rearranges response_info for printing proposes.
        Args:
            category (str): string inputs must be (films, people, planets, species, starships, vehicles)
            attribute (str): string inputs depending of category input(name, title, birth_year, eye_color,
            gender, hair_color, height, mass, skin_color, homeworld, films, species, starships,
            vehicles, created, edited).
        """
        for i in self.response_info['results']:
            if category != 'films':
                self.get_output[i['name']] = i[attribute]
            else:
                self.get_output[f"title: {i['title']}"] = i[attribute]
            self.counter += 1

    def load_response(self, category):
        """load response form api to response_info variable.
        Args:
            category (str): gets response form api depending of category input.
        """
        self.response = requests.get(f"{self.settings.BASE_URL}/{category}")
        if self.response.status_code == 200:
            self.response_info = self.response.json()

    def load_next_response(self):
        """load response next page if available form api to response_info variable.
        """
        if self.response_info['next']:
            self.response = requests.get(self.response_info['next'])
            self.response_info = self.response.json()

    def desc(self):
        """sorts dict in descending by value and returns it as a list of tuples.
        """
        self.get_output = sorted(sorted((value, key) for (key, value) in self.get_output.items()), reverse=True)

    def asc(self):
        """sorts dict in ascending by value and returns it as a list of tuples.
        """
        self.get_output = sorted((value, key) for (key, value) in self.get_output.items())

    def result_printer(self):
        """prints output depending of the type of output collected form the api.
        """
        for i in self.output:
            for item, value in i.items():
                if not isinstance(value, list) and "http://" not in value:
                    print(f"{item} : {value}")
            print(20 * '-')

    def get_result_printer(self):
        """prints get_output depending of the type of output collected form the api.
        """
        if isinstance(self.get_output, list):
            for value, key in self.get_output:
                print(value, key)
        else:
            for key, value in self.get_output.items():
                print(value, key)
