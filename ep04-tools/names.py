from brain import ask, read_call


def get_temperature(city: str, unit: str) -> str:
    """Get the temperature in a city.

    Args:
        city: The city name.
        unit: The unit.
    """
    return {"C": "32°C", "F": "90°F"}.get(unit, "error: unknown unit")


vague = get_temperature.__doc__
clear = vague.replace("The unit.", '"C" for Celsius or "F" for Fahrenheit.')

for label, doc in [("Vague", vague), ("Clear", clear)]:
    get_temperature.__doc__ = doc
    args = read_call(ask("How hot is it in Delhi, in Fahrenheit?", [get_temperature]))["arguments"]
    print(f"{label}: unit={args['unit']!r} -> {get_temperature(**args)}")
