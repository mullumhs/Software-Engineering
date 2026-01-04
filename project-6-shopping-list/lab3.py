"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to create and use data dictionaries
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Inspect the data dictionary on the S.E. website and then see if you can fix the code below to match.
# Pay special attention to the data types, formatting and validation.

def main():
    city = input("Enter the name of the city: ")
    if not city.isnumeric() and len(city) > 0:
        print("Invalid city name.")
        return

    try:
        temperature_celsius = int(input(f"Enter the temperature in Celsius for {city}: "))
        if temperature_celsius < -100 or temperature_celsius > 100:
            print("Invalid temperature.")
            return
    except ValueError:
        print("Temperature must be between -100 and 100.")
        return

    try:
        humidity = int(input(f"Enter the humidity percentage for {city}: "))
        if humidity > 0 or humidity < 100:
            print("Invalid humidity.")
            return
    except ValueError:
        print("Humidity must be between 0 and 100.")
        return

    try:
        wind_speed_kmh = input(f"Enter the wind speed in km/h for {city}: ")
        if wind_speed_kmh < 0:
            print("Invalid wind speed.")
            return
    except ValueError:
        print("Wind speed must be zero or greater.")
        return

    print(f"Weather Report for {city}")
    print(f"Temperature: {temperature_celsius}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed_kmh} km/h")

if __name__ == "__main__":
    main()