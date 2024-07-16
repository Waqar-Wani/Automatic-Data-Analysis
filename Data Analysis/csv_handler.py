import pandas as pd
import io

def parse_csv(contents):
    decoded = io.StringIO(contents.decode('utf-8'))
    df = pd.read_csv(decoded)
    return df
