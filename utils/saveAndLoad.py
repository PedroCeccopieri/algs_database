import pandas as pd
import json as js
import os

path = f"{os.path.dirname(os.path.dirname(__file__))}\database"

def save(df, file):
    result = df.to_json(orient="columns")
    parsed = js.loads(result)

    with open(path + f"\{file}.json", "w") as write_file:
        js.dump(parsed, write_file, indent=2)

def load(file):

    files = [i[0:len(i)-5] for i in os.listdir(path)]
    
    if (file in files):
        return pd.read_json(path + f"\{file}.json").astype({'name': 'string','top': 'object', 'side': 'object', 'algs': 'object'})
    else:
        print("file not found")
        return pd.DataFrame(columns = ['name','top', 'side', 'algs']).astype({'name': 'string','top': 'object', 'side': 'object', 'algs': 'object'})
