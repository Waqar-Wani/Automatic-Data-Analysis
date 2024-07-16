import base64
from csv_handler import parse_csv
from xls_handler import parse_xls, parse_xlsx
from json_handler import parse_json
from xml_handler import parse_xml
from sql_handler import execute_sql

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = parse_csv(decoded)
        elif 'xls' in filename:
            df = parse_xls(decoded)
        elif 'xlsx' in filename:
            df = parse_xlsx(decoded)
        elif 'json' in filename:
            df = parse_json(decoded)
        elif 'xml' in filename:
            df = parse_xml(decoded)
        elif 'sql' in filename:
            df = execute_sql(decoded)
        else:
            return None, 'Unsupported file type'
    except Exception as e:
        print(e)
        return None, 'There was an error processing this file.'
    
    if df is not None:
        file_info = {
            'File Name': filename,
            'File Size': len(decoded),
            'File Type': filename.split('.')[-1],
            'Number of Rows': df.shape[0],
            'Number of Columns': df.shape[1]
        }
    else:
        file_info = None
    
    return df, file_info
