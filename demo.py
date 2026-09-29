import json
from openai import AzureOpenAI, NotFoundError

client = AzureOpenAI(
    api_key="",
    azure_endpoint="",
    api_version="2025-04-14"
)

# Python function
def get_weather(city):
    return f"{city}: 27°C, Cloudy"


# Tell Azure AI about the function
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather of a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]


# User question
messages = [
    {"role": "user", "content": "Weather in Bangalore?"}
]


# AI decides whether to call the function
try:
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
except NotFoundError as exc:
    raise RuntimeError(
        "Azure OpenAI returned 404. Check that the deployment name 'my-gpt41' exists "
        "in your Azure OpenAI resource and that the endpoint is correct."
    ) from exc

msg = response.choices[0].message
print("AI response ---msg vamsi:", msg.content)


# Python executes the function requested by AI
if msg.tool_calls:

    call = msg.tool_calls[0]

    args = json.loads(call.function.arguments)

    print("AI requested:", call.function.name)
    print("Arguments:", args)

    result = get_weather(args["city"])

    print("Python result:", result)