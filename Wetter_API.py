from pyowm.owm import OWM
from pyowm.utils.config import get_config_from
from pyowm.utils.config import get_default_config_for_subscription_type

config_dict = get_default_config_for_subscription_type('free')
owm = OWM('1a8b1d6e34be977e469e42517727e81b', config_dict)

owm.supported_languages

config_dict = owm.configuration

version_tuple = (major, minor, patch) = owm.version

reg = owm.city_id_registry()
#list_of_tuples = munich = reg.ids_for('Munich', country='DE')                 # only one: [ (2643743,, 'London, GB') ]
#list_of_tuples = reg.ids_for('london', country='GB', matching='like')           # mehrere Einträge mit bes. string im Namen
#id_of_london_city = list_of_tuples[0][0]

list_of_locations = reg.locations_for('munich', country='DE')
munich = list_of_locations[0] # IDs als Liste
lat = munich.lat   # Längengrad München
lon = munich.lon   # Breitengrad München
print(lat, lon)
#print(id_of_london_city)
#print (list_of_tuples[0:5])
#print(lat, lon)

mgr = owm.weather_manager()
one_call = mgr.one_call(lat, lon)



observation = mgr.weather_at_place('Munich,DE')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
print(weather.detailed_status)  # detailed version of status (eg. 'light rain')


weather = mgr.weather_at_place('Munich,DE').weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
temp_dict_kelvin['temp_min']
temp_dict_kelvin['temp_max']
temp_dict_fahrenheit = weather.temperature('fahrenheit')  # a dict in Fahrenheit units
temp_dict_celsius = weather.temperature('celsius')  # guess?
print(temp_dict_celsius)

#wind_dict_in_meters_per_sec = observation.weather.wind()   # Default unit: 'meters_sec'
#wind_dict_in_meters_per_sec['speed']
#wind_dict_in_meters_per_sec['deg']
#wind_dict_in_meters_per_sec['gust']
#wind_dict_in_miles_per_h = mgr.weather_at_place('Munich,DE').wnd(unit='miles_hour')
#wind_dict_in_knots = mgr.weather_at_place('Munich,DE').wnd(unit='knots')
#wind_dict_in_beaufort = mgr.weather_at_place('Munich,DE').wnd(unit='beaufort')  # Beaufort is 0-12 scale

#feels_like_temp = one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None) #Ex.: 7.7
#print('gefühlte Temperatur am Morgen in München', feels_like_temp, '°Celsius')


rain_dict = mgr.weather_at_place('Munich,DE').observation.rain
rain_dict['1h']
rain_dict['3h']

sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
sunrise_iso = weather.sunrise_time(timeformat='iso')
sunrise_date = weather.sunrise_time(timeformat='date')
sunrset_unix = weather.sunset_time()  # default unit: 'unix'
sunrset_iso = weather.sunset_time(timeformat='iso')
sunrset_date = weather.sunset_time(timeformat='date')

print(sunrise_unix)
