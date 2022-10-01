# Прогноз погоды

import pyowm

city = input('Введите город: ')

owm = pyowm.OWM('99999999999999999999999999999999') # api key
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp'] # получение temp

print(city + ', температура: ' + str(temperature))
print('Погодные условия: '+ w.get_detailed_status())
