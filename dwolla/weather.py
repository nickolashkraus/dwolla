"""Module for 'weather' command."""
import pprint

import click

from .api import OpenWeatherMapAPI


@click.command()
@click.option('--name', help='Name of the city')
@click.option('--id', help='ID of the city')
@click.option(
    '--coordinates',
    nargs=2,
    help='Coordinates of the city (latitude and longitude)')
@click.option('--zip', help='Zip code of the city')
def weather(*args, **kwargs) -> None:
    """
    Retrieve the current weather data for a city.

    Examples:\n
    \b
    # Get the current weather data by city name.
    dwolla weather --name Chicago

    \b
    # Get the current weather data by city id.
    dwolla weather --id 4887442

    \b
    # Get the current weather data by geographic coordinates.
    dwolla weather --coordinates 41.506149 -87.635597

    \b
    # Get the current weather data by ZIP code.
    dwolla weather --zip 60611

    """
    api = OpenWeatherMapAPI()
    if kwargs['name']:
        r = api.get_by_name(kwargs['name'])
    elif kwargs['id']:
        r = api.get_by_id(kwargs['id'])
    elif kwargs['coordinates']:
        r = api.get_by_coordinates(kwargs['coordinates'])
    elif kwargs['zip']:
        r = api.get_by_zip(kwargs['zip'])
    else:
        exit(1)

    pprint.pprint(r)
