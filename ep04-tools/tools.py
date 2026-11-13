def get_weather(city: str) -> str:
    """Get today's weather for a city.

    Args:
        city: The city name.
    """
    return {"Delhi": "32°C, sunny", "London": "11°C, rain"}.get(city, "error: unknown city")


def get_time(city: str) -> str:
    """Get the current local time in a city.

    Args:
        city: The city name.
    """
    return {"Delhi": "15:00", "London": "09:30"}.get(city, "error: unknown city")


def check_calendar(day: str) -> str:
    """List the events in my calendar on a given day.

    Args:
        day: The day of the week, like Monday.
    """
    return {"Friday": "9:00 team meeting, 13:00 lunch with Asha"}.get(day, "no events")
