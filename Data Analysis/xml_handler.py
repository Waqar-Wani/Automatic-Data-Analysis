import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml(contents):
    try:
        root = ET.fromstring(contents)
        data = []
        for child in root:
            row = {}
            for item in child:
                row[item.tag] = item.text
            data.append(row)
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(e)
        return None
