from .starwars_search import StarWarsSearch

import sys

import argparse


class ApiUserCli:
    """Api command-line interface:
        the command-line interface excepts input in str and prints searched values.

        commands:
            (search, get-films, get-people, get-planets, get-species, get-starships, get-vehicles get-string)

         example:
            "search people name Skywalker" -> prints all people name includes Skywalker.
            "get-films episode_id" -> prints all films and episode_id.
            "get-films episode_id (optional: -a(--asc),-d(--desc))"
            -> prints all films and episode_id (optional: ascending/descending by episode_id).
    """
    def __init__(self):
        """initialize ApiUserCli class

        initializes an instance of StarWarsSearch() class
        and initializes get_args() function
        """
        self.api_instance = StarWarsSearch()
        self.get_args()

    def get_search(self, category, attribute, asc=False, desc=False):
        """searches category by (category, attribute)

        Args:
            category (str): a input category in the api by user command-line interface.
            attribute (str): a input attribute in the api by user command-line interface.
            asc (bool, optional): sorts dict in ascending by value. Defaults to False.
            desc (bool, optional): sorts dict in descending by value. Defaults to False.
        """
        self.api_instance.get_function(category, attribute)
        if asc:
            self.api_instance.asc()
        if desc:
            self.api_instance.desc()
        self.api_instance.get_result_printer()

    def search(self, category, attribute, filters):
        """searches category by attribute result filtered by input parameter (category, attribute, filters)

        Args:
            category (str): a input category in the api by user command-line interface.
            attribute (str): a input attribute in the api by user command-line interface.
            filters (str): a input filter in the api by user command-line interface.
        """
        self.api_instance.starwars_search(category, attribute, filters)
        self.api_instance.result_printer()

    def get_args(self):
        """executes a specific function based on input command-line interface.
        """
        if sys.argv[1] == 'search':
            self.execute_argparse_search()
        elif "get-" in sys.argv[1]:
            self.execute_argparse_get()

    def execute_argparse_search(self):
        """executes search function depending of the input (input must be correct).
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('search', help='a function execution, example: search people name Skywalker')
        parser.add_argument('category', help='search category, example: people')
        parser.add_argument('attribute', help='search attribute, example: name')
        parser.add_argument('filters', help='search filters, example: Skywalker')
        args = parser.parse_args()
        self.search(args.category, args.attribute, args.filters)

    def execute_argparse_get(self):
        """executes get-search function depending of the input (input must be correct).
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('get_category', help='search category, example: get-films episode_id')
        parser.add_argument('attribute', help='search by attribute')
        parser.add_argument('-a', '--asc', help='sort return values ascending', action="store_true")
        parser.add_argument('-d', '--desc', help='sort return values descending', action="store_true")
        args = parser.parse_args()
        self.get_search(args.get_category.strip('get-'), args.attribute, args.asc, args.desc)
