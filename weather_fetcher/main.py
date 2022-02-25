# TODO: upgrade to GUI
import requests

API_KEY = "58a3b8d841836ab66b729355f6668a6c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&lang=ru&units=metric"
response = requests.get(request_url)

def degToCompass(degrees):
    val=int((degrees/45)+.5)
    arr=["С","СВ","В","ЮВ","Ю","ЮЗ","З","СЗ"]
    return arr[(val % 8)]

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = int(data['main']['temp'])
    wind = data['wind']['speed']
    windDegrees = data['wind']['deg']
    humidity = data['main']['humidity']
    print('Погода: ', weather)
    print('Температура: ', temp, '°C')
    print('Ветер: ', wind, ' м/с ', degToCompass(windDegrees))
    print('Влажность', humidity, '%')
else:
    print("An error occured")