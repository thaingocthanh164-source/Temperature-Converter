from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

choice = input("Convert (C/F): ").strip().upper()

if choice == "C":
    celsius = float(input("Enter Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {result:.2f}°F")
elif choice == "F":
    fahrenheit = float(input("Enter Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {result:.2f}°C")
else:
    print("Invalid option.")
