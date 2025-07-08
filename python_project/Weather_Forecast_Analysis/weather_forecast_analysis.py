import os
import json

WEATHER_DATA_PATH = r"C:\Users\Dell\python-core\python_project\Weather_Forecast_Analysis\weather_forecast_data.txt"

def load_weather_data():
    if os.path.exists(WEATHER_DATA_PATH):
        try:
            with open(WEATHER_DATA_PATH, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_weather_data(weather_data):
    with open(WEATHER_DATA_PATH, "w") as file:
        json.dump(weather_data, file, indent=4)

def collect_weather_data():
    print("-----> WEATHER DATA ANALYSIS <----")
    weather_data = []

    num_days = int(input("How many days of weather data you want to enter? "))

    for i in range(num_days):
        print(f"Enter data for Day {i + 1}:")
        date = input("Date (YYYY-MM-DD): ")
        temp = float(input("Temperature (°C): "))
        rainfall = float(input("Rainfall (mm): "))
        humidity = float(input("Humidity (%): "))

        weather_data.append({
            "date": date,
            "temp": temp,
            "rainfall": rainfall,
            "humidity": humidity
        })

    return weather_data  

def display_stored_data(weather_data):
    print("Weather Data Records:")
    for i, day in enumerate(weather_data, 1):
        print(f"\nRecord {i}:")
        print(f"  Date: {day['date']}")
        print(f"  Temperature: {day['temp']}°C")
        print(f"  Rainfall: {day['rainfall']}mm")
        print(f"  Humidity: {day['humidity']}%")

def analyze_weather_data(weather_data):
    if not weather_data:
        print("\nNo weather data available for analysis")
        return
    
    temps = [day['temp'] for day in weather_data]
    rains = [day['rainfall'] for day in weather_data]
    humids = [day['humidity'] for day in weather_data]
    
    # Calculate averages
    avg_temp = sum(temps) / len(temps)
    total_rain = sum(rains)
    avg_humid = sum(humids) / len(humids)
    
    # Find extremes
    max_temp = max(temps)
    min_temp = min(temps)
    max_rain = max(rains)

    hottest_day = [day for day in weather_data if day['temp'] == max_temp][0]
    coldest_day = [day for day in weather_data if day['temp'] == min_temp][0]
    rainiest_day = [day for day in weather_data if day['rainfall'] == max_rain][0]
    
    print("\nWeather Data Analysis:")
    print(f"\nTemperature Analysis:")
    print(f"  Average: {avg_temp:.1f}°C")
    print(f"  Hottest: {hottest_day['date']} ({max_temp}°C)")
    print(f"  Coldest: {coldest_day['date']} ({min_temp}°C)")
    
    print(f"\nRainfall Analysis:")
    print(f"  Total: {total_rain}mm")
    print(f"  Max Daily: {rainiest_day['date']} ({max_rain}mm)")
    
    print(f"\nHumidity Analysis:")
    print(f"  Average: {avg_humid:.1f}%")
    
    if len(temps) > 1:
        trend = "rising" if temps[-1] > temps[0] else "falling" if temps[-1] < temps[0] else "stable"
        print(f"\nTemperature trend: {trend}")

def main():
    
    weather_data = load_weather_data()
    

    new_data = collect_weather_data()
    weather_data.extend(new_data)
    
    save_weather_data(weather_data)
    print(f"\n Weather data saved to '{WEATHER_DATA_PATH}'")
    
  
    display_stored_data(weather_data)
    analyze_weather_data(weather_data)
    
   
if __name__ == "__main__":
    main()
