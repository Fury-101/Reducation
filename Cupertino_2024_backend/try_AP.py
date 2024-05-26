import os
import sys
import parse_it

parse_it.get_curriculum()

AP_list = ["Chemistry", "Physics", "Biology", "Calculus AB", "Calculus BC", "Statistics", "Computer Science A", "Computer Science Principles", "English Language and Composition", "English Literature and Composition", "US History"]
AP_list = ['AP ' + x for x in AP_list]

for AP in AP_list:
    print(f"Getting curriculum for {AP}...")
    parse_it.get_curriculum(AP)