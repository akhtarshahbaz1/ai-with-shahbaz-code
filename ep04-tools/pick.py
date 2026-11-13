from brain import ask, read_call
from tools import check_calendar, get_time, get_weather

TOOLS = [get_weather, get_time, check_calendar]
FUNCTIONS = {tool.__name__: tool for tool in TOOLS}

for question in [
    "Is it raining in London today?",
    "What time is it in Delhi right now?",
    "What do I have on Friday?",
]:
    call = read_call(ask(question, TOOLS))
    name, args = call["name"], call["arguments"]
    print(question)
    print(f"  call:   {name}({args})")
    print(f"  result: {FUNCTIONS[name](**args)}")
