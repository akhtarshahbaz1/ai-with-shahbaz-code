import inspect

from tools import check_calendar, get_time, get_weather

SAFE = {tool.__name__: tool for tool in [get_weather, get_time, check_calendar]}
ASK_FIRST = {"send_email", "pay", "delete_file"}


def check(name, args):
    if name in ASK_FIRST:
        return "paused: ask a human first"
    if name not in SAFE:
        return "refused: not an allowed tool"
    if set(args) != set(inspect.signature(SAFE[name]).parameters):
        return "refused: wrong arguments"
    return SAFE[name](**args)


for name, args in [
    ("get_weather", {"city": "London"}),
    ("delete_everything", {}),
    ("get_time", {"town": "Delhi"}),
    ("send_email", {"to": "boss@example.com", "text": "Running late"}),
]:
    print(f"{name} -> {check(name, args)}")
