rain = input("Is it raining? (yes/no): ").lower()
umbrella = input("Do you have an umbrella? (yes/no): ").lower()


if rain == "yes" and umbrella == "yes":
    print("You can go outside!")
elif rain == "no" and umbrella == "yes":
    print("U r prepared af")
else:
    print("Better stay in.")