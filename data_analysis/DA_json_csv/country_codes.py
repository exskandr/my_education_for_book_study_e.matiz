# from pygal.i18n import COUNTRIES
# from pygal.maps.world import COUNTRIES
import pygal
# from pygal.maps.world import World
# from pygal_maps_world import i18n

from pygal_maps_world import i18n

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    # worldmap_chart = pygal.maps.world.World()
    # for code, name in worldmap_chart:

    for code, name in i18n.COUNTRIES:

    # for code, name in COUNTRIES.items():
        if name == country_name:
            print(code)
            return code
    # If the country wasn't found, return None.
    return None
