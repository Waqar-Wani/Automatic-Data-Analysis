import dash
from dash import html, dcc, Input, Output, dash_table
from upload import parse_contents
import io

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("File Upload and Print"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='file-info'),
    html.Div(id='output-data')
])

@app.callback(Output('output-data', 'children'),
              Output('file-info', 'children'),
              Input('upload-data', 'contents'),
              Input('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        df, file_info = parse_contents(contents, filename)
        if file_info is not None:
            file_info_div = html.Div([
                html.H3("File Information:"),
                html.Table([
                    html.Tr([html.Td(key), html.Td(str(value))]) for key, value in file_info.items()
                ])
            ])
        else:
            file_info_div = html.Div("File Information Not Available")
        
        if df is not None:
            data_table = html.Div([
                html.H5(f'Table view of {filename}:'),
                dash_table.DataTable(
                    columns=[{'name': col, 'id': col} for col in df.columns],
                    data=df.to_dict('records')
                )
            ])
        else:
            data_table = html.Div("No data to display.")
        
        return data_table, file_info_div
    else:
        return html.Div("Upload a file to display data."), html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
