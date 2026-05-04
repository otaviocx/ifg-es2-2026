import requests
import pandas as pd

def get_temperature(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['hourly']

def format_temperature(temperature):
    return f"{temperature:.2f}°C"

def parse_temperatures(latitude, longitude):
    data = get_temperature(latitude, longitude)
    temperatures = data['temperature_2m']
    times = data['time']
    return pd.DataFrame({
        'Time': times,
        'Temperature': [format_temperature(temp) for temp in temperatures]
    })

if __name__ == "__main__":
    df = parse_temperatures(-16.665873, -49.2573415)
    print(df)
