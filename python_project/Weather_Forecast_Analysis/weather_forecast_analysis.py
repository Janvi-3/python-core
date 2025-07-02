# Simple Weather Forecast Analysis Program

def main():
    # Sample weather data for a week (day: temperature in °C)
    weather_data = {
        "Monday": 20,
        "Tuesday": 22,
        "Wednesday": 19,
        "Thursday": 24,
        "Friday": 23,
        "Saturday": 25,
        "Sunday": 21
    }

    # Display the weather data
    print("=== Weekly Weather Forecast ===")
    for day, temperature in weather_data.items():
        print(f"{day}: {temperature}°C")

    # Calculate the average temperature
    total_temperature = sum(weather_data.values())
    average_temperature = total_temperature / len(weather_data)
    print(f"\nAverage Temperature: {average_temperature:.2f}°C")

    # Find the day with the highest temperature
    highest_temp_day = max(weather_data, key=weather_data.get)
    highest_temp_value = weather_data[highest_temp_day]
    print(f"The highest temperature was on {highest_temp_day} with {highest_temp_value}°C.")

if __name__ == "__main__":
    main()  # Run the main function
