from openai import OpenAI

API_KEY = "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"
model = 'mistral-7b-instruct'
client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

'''
prompt = "Please give me a list of the AP calculus AB currciulum. Only include the names of the units, nothing else."

messages = [
    {
        "role" : "system",
        "content" : (
            "You are an artificial intelligence and you need to engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role" : "user",
        "content" : (
            prompt
        ),
    },
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=4000
)

print(response)

print(response.choices[0].message.content)
'''

def get_response(PROMPT):
    PROMPT += " This was a the response to the previously stated question. Please provide a detailed feedback to the user in a friendly and helpful manner. Then you should provide and example of a model response. You should not exceed 500 words."
    messages = [
        {
            "role" : "system",
            "content" : (
                "You are an artificial intelligence and you need to engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {
            "role" : "user",
            "content" : (
                PROMPT
            ),
        },
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1000
    )

    return response.choices[0].message.content
