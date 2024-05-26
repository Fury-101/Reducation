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

def get_response_mcq(PROMPT):
    print("Making MCQ")
    PROMPT += " Here is a large piece of information. I want you to create ONE multiple choice guiding question with 4 answer choices regarding the content. The question should be clear and concise, and the answer choices should be relevant to the question. Please provide the correct answer in the format 'Answer: [LETTER]'. Please limit your response to 100 words."
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

    response = response.choices[0].message.content
    print("MCQ created")

    question = {'options':[]}
    response = response.split('\n')
    for line in response:
        if 'Question:' in line:
            question['q'] = line.split('Question: ')[1]
        if 'Answer:' in line:
            question['ans'] = ord(line.split('Answer: ')[1][0]) - ord('A')
        if 'A)' in line or 'B)' in line or 'C)' in line or 'D)' in line:
            question['options'].append(') '.join(line.split(') ')[1:]))

    return question

def get_response_frq(PROMPT):
    print("Making FRQ")
    PROMPT += " Here is a large piece of information. I want you to create a free response question to really test a learner's understanding of this topic. Only ask questions that can be answered through a textual response. Please limit your question to 100 words."
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
    print("FRQ created")

    return response.choices[0].message.content.replace("Question: ", "")

'''
corpus = open('tmp.txt', 'r').read()
print(get_response_frq(corpus))
'''
