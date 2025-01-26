import Weather_app

API_KEY = 'your_openweather_api_key'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")
    else:
        print("City not fount.")

city = input("Enter city: ")
get_weather(city)