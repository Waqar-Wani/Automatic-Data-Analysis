import pandas as pd
import json

def parse_json(contents):
    try:
        # Decode the contents from bytes to string
        decoded = contents.decode('utf-8')
        # Parse the JSON data
        data = json.loads(decoded)
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(e)
        return None
