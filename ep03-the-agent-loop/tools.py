import json

from transformers.utils import get_json_schema


def get_weather(city: str) -> str:
    """Get today's weather for a city.

    Args:
        city: The city name.
    """
    return {"Delhi": "32°C, sunny", "London": "11°C, rain"}.get(city, "error: unknown city")


if __name__ == "__main__":
    schema = get_json_schema(get_weather)["function"]
    print(schema["name"], "-", schema["description"])
    print(json.dumps(schema["parameters"]["properties"]))
