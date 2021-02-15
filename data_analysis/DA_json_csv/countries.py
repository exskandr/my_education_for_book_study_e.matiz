# from pygal.i18n import COUNTRIES
from pygal.maps.world import COUNTRIES

from pygal_maps_world import i18n



# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    """Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # Если страна не найдена, вернуть None.
        return None

    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('Afghanistan'))

