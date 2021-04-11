from pyowm.owm import OWM
from pyowm.utils.config import get_config_from
from pyowm.utils.config import get_default_config_for_subscription_type
from pyowm.utils import timestamps, formatting

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

print("city: " +str(list_of_locations))

#print(id_of_london_city)
#print (list_of_tuples[0:5])
#print(lat, lon)

mgr = owm.weather_manager()
one_call = mgr.one_call(lat, lon)


observation = mgr.weather_at_place('Munich,DE')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
print("timestamp: " + str(weather))
print("weather status: " + weather.detailed_status)  # detailed version of status (eg. 'light rain')


# client = weather.status()
    #subscribe(client)
    #client.loop_forever()

weather = mgr.weather_at_place('Munich,DE').weather
temp_dict_kelvin = observation.weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
temp_dict_kelvin['temp_min']
temp_dict_kelvin['temp_max']
temp_dict_fahrenheit = observation.weather.temperature('fahrenheit')  # a dict in Fahrenheit units
temp_dict_celsius = observation.weather.temperature('celsius')  # guess?
print("temperature: " + str(temp_dict_celsius))

wind_dict_in_meters_per_sec = observation.weather.wind()   # Default unit: 'meters_sec'
wind_dict_in_meters_per_sec['speed']
wind_dict_in_meters_per_sec['deg']
#wind_dict_in_meters_per_sec['gust']

print("wind: " + str(wind_dict_in_meters_per_sec))

rain_dict = mgr.weather_at_place('Munich,DE').weather.rain
#rain_dict[]
#rain_dict['3h']
#rain_dict['3h']

print("rain (in mm): " + str(rain_dict))

sunrise_unix = observation.weather.sunrise_time()  # default unit: 'unix'
sunrise_iso = observation.weather.sunrise_time(timeformat='iso')
sunrise_date = observation.weather.sunrise_time(timeformat='date')
sunrset_unix = observation.weather.sunset_time()  # default unit: 'unix'
sunrset_iso = observation.weather.sunset_time(timeformat='iso')
sunrset_date = observation.weather.sunset_time(timeformat='date')

print("sunrise: " + sunrise_iso)
print("sunset: " + sunrset_iso)

one_call.current.humidity
print("humidity in %: " + str(one_call.current.humidity))

pressure_dict = observation.weather.pressure
pressure_dict['press']
pressure_dict['sea_level']
print("pressure: " + str(pressure_dict))


