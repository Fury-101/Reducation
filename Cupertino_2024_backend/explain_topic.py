import os
import sys
import json
import time
import perplexity_api_explanation
import parse_it
from tqdm import tqdm

'''
args = sys.argv
if len(args) < 2:
    print("Usage: python3 explain_topic.py <topic>")
    sys.exit(1)

topic = ' '.join(args[1:])
'''

def explain_topic(topic):
    PROMPT = (lambda x: "Explain this subtopic: " + x + " of topic " + topic)

    C = {}

    # Get the curriculum
    curriculum = parse_it.get_curriculum(topic)
    print("Curriculum Acquired")
    for i, unit in tqdm(enumerate(curriculum.keys()), total=len(curriculum)):
        title = "Unit " + str(i+1) + ": " + unit
        C[title] = {}
        for j, T in enumerate(curriculum[unit]):
            section = f"{i+1}.{j+1} - {T}"
            C[title][section] = perplexity_api_explanation.get_response(PROMPT(T))

    return C