# Read the temperature and normalize the yes/no answer.
temperature = float(input("Enter current temperature (F): "))
rain_answer = input("Is it raining (yes/no)? ").strip().lower()

if rain_answer not in ("yes", "no"):
    print("Please enter yes or no for rain.")
else:
    raining = rain_answer == "yes"

    # Test extreme heat first so it takes priority regardless of rain.
    if temperature > 100:
        print("EXTREME HEAT WARNING: Stay indoors!")
    elif temperature > 85 and raining:
        print("Warm rain — watch for flash floods.")
    elif temperature > 85 and not raining:
        print("Hot and dry — stay hydrated.")
    elif temperature >= 60 and raining:
        print("Grab an umbrella!")
    elif temperature >= 60 and not raining:
        print("Nice weather — enjoy your day!")
    elif temperature >= 32:
        # Earlier branches already handled temperatures of 60 or higher.
        print("It's cold — bundle up!")
    else:
        print("FREEZE WARNING: Roads may be icy!")
