temperature = int(input("Enter Temperature: "))
humidity = int(input("Enter Humidity: "))

print("Too Cold") if temperature <= 12 and humidity <= 70 else print("Too Hot!")