import requests

API_KEY = "your_api_key_here"  # Free OpenWeatherMap API key
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data.get("main"):
    print(f"Weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
else:
    print("City not found or API error.")
