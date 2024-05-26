import os
import sys
import perplexity_api_curriculum

'''
args = sys.argv
if len(args) < 2:
    print("Usage: python parse_it.py <topic>")
    sys.exit(1)
topic = ' '.join(args[1:])
'''

def get_curriculum(topic = "How to do Taxes"):
    cnt = 0
    while cnt < 10:
        text = perplexity_api_curriculum.get_response(f"Please give me a list of the {topic} currciulum. Only list the unit names and their subunits. Please give them in a simple easy to understand format. For example, Unit 1 [NAME] : Subunit 1 [NAME], Subunit 2 [NAME], Subunit 3 [NAME]...' Also, please provide short unit names. PLEASE USE THE SPECIFIED FORMAT OF 'Unit [NUMBER] [NAME] : Subunit [NUMBER] [NAME], Subunit [NUMBER] [NAME], Subunit [NUMBER] [NAME]...'.")
        with open("tmp.txt", "w") as f:
            f.write(text)
        cnt += 1
        output_file_name = f"responses/{topic}.txt"
        # if file already exists, increment the number
        i = 1
        while os.path.exists(output_file_name):
            output_file_name = f"responses/{topic} ({i}).txt"
            i += 1

        L = text.split("\n\n")

        unit_names = {}
        num_units = 0
        idx = 1

        end_it = False
        while idx < len(L) and f'Unit {num_units + 1}' in L[idx]:
            unit_name = L[idx].split('\n')[0]
            unit_name = f': '.join(unit_name.split(f': ')[1:])
            # remove all *s at the end
            while unit_name[-1] == '*':
                unit_name = unit_name[:-1]
            unit_names[unit_name] = []
            # get all subunits
            for line in L[idx].split('\n')[1:]:
                if 'Subunit' in line:
                    unit_names[unit_name].append(': '.join(line.split(': ')[1:]))
            if len(unit_names[unit_name]) == 0:
                end_it = True
                break
            num_units += 1
            idx += 1

        if num_units < 3 or num_units > 9 or end_it:
            print("No units detected, trying again...")
            continue


        print("Total number of units:", num_units)
        #print("Unit names:", unit_names)

        with open(output_file_name, "w") as f:
            f.write(text)

        print(f"Saved response to {output_file_name}")
        return unit_names
        break
    print("Failed to get curriculum after 10 attempts.")  