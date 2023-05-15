
#!/usr/bin/env python3

import argparse
from country import Country
from city import City
from place import Place

if __name__ == '__main__':
    pass

def create_country(args):
    country_manager = Country()
    country_manager.add_country(args.name)
    country_manager.close_connection()

def list_countries(args):
    country_manager = Country()
    country_manager.list_countries()
    country_manager.close_connection()

def search_countries(args):
    country_manager = Country()
    country_manager.search_countries(args.search_term)
    country_manager.close_connection()

def create_city(args):
    city_manager = City()
    city_manager.add_city(args.name, args.country_id)
    city_manager.close_connection()

def list_cities(args):
    city_manager = City()
    city_manager.list_cities(args.country_id)
    city_manager.close_connection()

def search_cities(args):
    city_manager = City()
    city_manager.search_cities(args.search_term)
    city_manager.close_connection()

def create_place(args):
    place_manager = Place()
    place_manager.add_place(args.name, args.city_id)
    place_manager.close_connection()

def list_places(args):
    place_manager = Place()
    place_manager.list_places(args.city_id)
    place_manager.close_connection()

def search_places(args):
    place_manager = Place()
    place_manager.search_places(args.search_term)
    place_manager.close_connection()

def filter_places(args):
    place_manager = Place()
    place_manager.filter_places_by_type(args.object_type)
    place_manager.close_connection()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Travel Database CLI')

    subparsers = parser.add_subparsers(title='Commands', dest='command')

    # Create Country command
    create_country_parser = subparsers.add_parser('create-country', help='Create a new country')
    create_country_parser.add_argument('name', type=str, help='Country name')
    create_country_parser.set_defaults(func=create_country)

    # List Countries command
    list_countries_parser = subparsers.add_parser('list-countries', help='List all countries')
    list_countries_parser.set_defaults(func=list_countries)

    # Search Countries command
    search_countries_parser = subparsers.add_parser('search-countries', help='Search for countries')
    search_countries_parser.add_argument('search_term', type=str, help='Search term')
    search_countries_parser.set_defaults(func=search_countries)

    # Create City command
    create_city_parser = subparsers.add_parser('create-city', help='Create a new city')
    create_city_parser.add_argument('name', type=str, help='City name')
    create_city_parser.add_argument('country_id', type=int, help='ID of the country')
    create_city_parser.set_defaults(func=create_city)

    # List Cities command
    list_cities_parser = subparsers.add_parser('list-cities', help='List all cities')
    list_cities_parser.add_argument('country_id', type=int, nargs='?', help='ID of the country')
    list_cities_parser.set_defaults(func=list_cities)

    # Search Cities command
    search_cities_parser = subparsers.add_parser('search-cities', help='Search for cities')
    search_cities_parser.add_argument('search_term', type=str, help='Search term')
    search_cities_parser.set_defaults(func=search_cities)

    # Create Place command
    create_place_parser = subparsers.add_parser('create-place', help='Create a new place')
    create_place_parser.add_argument('name', type=str, help='Place name')
    create_place_parser.add_argument('city_id', type=int, help='ID of the city')
    create_place_parser.set_defaults(func=create_place)

    # List Places command
    list_places_parser = subparsers.add_parser('list-places', help='List all places')
    list_places_parser.add_argument('city_id', type=int, nargs='?', help='ID of the city')
    list_places_parser.set_defaults(func=list_places)

    # Search Places command
    search_places_parser = subparsers.add_parser('search-places', help='Search for places')
    search_places_parser.add_argument('search_term', type=str, help='Search term')
    search_places_parser.set_defaults(func=search_places)

    # Filter Places command
    filter_places_parser = subparsers.add_parser('filter-places', help='Filter places by type')
    filter_places_parser.add_argument('object_type', type=str, help='Object type')
    filter_places_parser.set_defaults(func=filter_places)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()