import pandas as pd
import io

def parse_xls(contents):
    decoded = io.BytesIO(contents)
    df = pd.read_excel(decoded)
    return df

def parse_xlsx(contents):
    decoded = io.BytesIO(contents)
    df = pd.read_excel(decoded)
    return df
