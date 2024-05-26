import os
import sys
import json
import time
import explain_topic
import perplexity_api_grade_frq
import perplexity_api_create_questions
import Relevant_Youtube_api
from tqdm import tqdm
from flask import Flask, request, jsonify 
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get_curriculum', methods=['POST'])
@cross_origin()
def get_curriculum():
    try:
        # Retrieve the string from the request data
        data = request.get_json()
        input_string = data.get('input_string')
        
        if input_string:
            if input_string in os.listdir('saved_data'):
                C = json.load(open(f'saved_data/{input_string}/C.json', 'r'))
                Q_mcq = json.load(open(f'saved_data/{input_string}/Q_mcq.json', 'r'))
                Q_frq = json.load(open(f'saved_data/{input_string}/Q_frq.json', 'r'))
                YT_vids = json.load(open(f'saved_data/{input_string}/YT_vids.json', 'r'))
                return jsonify({'C': C, 'Q_mcq': Q_mcq, 'Q_frq': Q_frq, 'YT_vids': YT_vids}), 200

            # Process the string (replace this with your own logic)
            processed_string = input_string

            # Retrieve the curated response
            C = explain_topic.explain_topic(processed_string)
            print("Got C")
            Q_mcq = {}
            Q_frq = {}
            YT_vids = {}

            for unit in tqdm(C.keys()):
                Q_mcq[unit] = []
                for section in C[unit].keys():
                    Q_mcq[unit].append({"name": section, "expanded": False, "mcq" : [perplexity_api_create_questions.get_response_mcq(C[unit][section])]})
            print("GOt Q MCQ")

            for unit in tqdm(C.keys()):
                Q_frq[unit] = perplexity_api_create_questions.get_response_frq(unit)
            print("GOt Q frq")

            for unit in tqdm(C.keys()):
                YT_vids[unit] = []
                for section in C[unit].keys():
                    YT_vids[unit].append({"name": section, "expanded": False, "videos" : Relevant_Youtube_api.search_youtube(section)})
            print("GOt YT")

            os.makedirs(f'saved_data/{input_string}', exist_ok=True)
            json.dump(C, open(f'saved_data/{input_string}/C.json', 'w'))
            json.dump(Q_mcq, open(f'saved_data/{input_string}/Q_mcq.json', 'w'))
            json.dump(Q_frq, open(f'saved_data/{input_string}/Q_frq.json', 'w'))
            json.dump(YT_vids, open(f'saved_data/{input_string}/YT_vids.json', 'w'))
            print(type(jsonify([C, Q_mcq, Q_frq, YT_vids])))
            return (
                jsonify([C, Q_mcq, Q_frq, YT_vids]),
                200
            )
        else:
            return (jsonify({'error': 'No input string provided'}), 400)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    
@app.route('/grade_frq', methods=['POST'])
@cross_origin()
def grade_frq():
    try:
        # Retrieve the string from the request data
        data = request.get_json()
        question = data.get('question')
        user_response = data.get('user_response')

        if question and user_response: 
            init_prompt = question + " " + user_response
            
            # Retrieve the curated response
            response = perplexity_api_grade_frq.get_response(init_prompt)

            return jsonify({'response': response}), 200
        else:
            return jsonify({'error': 'No input string provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)