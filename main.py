# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

with open("./nato_phonetic_alphabet.csv") as nato:
    # nato_df = pd.DataFrame(nato.read().splitlines()).reindex
    nato_list = nato.read().splitlines()
    new_list = [e.split(",") for e in nato_list[1:]]
    nato_map = {e[0]: e[1] for e in new_list}
    # print(nato_map)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Inter your name: ")
for litter in name:
    if litter in nato_map:
        print(f"{litter.upper()} は：{nato_map[litter.upper()]}の {litter.upper()}")
