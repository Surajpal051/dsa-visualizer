from dash import Dash, html, dcc,Input,Output,State
import plotly.graph_objects as go
from utils.randomarray import random_array
app = Dash(__name__)

## app layout
app.layout = html.Div(children=[
    dcc.Store(id='array-store'),
    html.H1(["DSA Visualizer"], style = {'textAlign':'center','marginBottom':'30px'}),
    html.Label('Algorithm', style={'fontWeight':'bold','fontSize':'20px'}),
    dcc.Dropdown(
        options = [
            {'label':'Bubble Sort','value':'Bubble Sort'},
            {'label':'Selection sort','value':'Selection sort'},
            {'label':'Merge Sort','value':'Merge Sort'},
            {'label':'Quick Sort','value':'Quick Sort'},
            {'label':'Binary Search','value':'Binary Search'},
            {'label':'Stack','value':'Stack'},
            {'label':'Queue','value':'Queue'},
            {'label':'Linked List','value':'Linked List'},
        ],
    ),
    html.Label('Size',style={'fontWeight':'bold','fontSize':'20px'}),
    html.Div(id='output_for_size'),
    dcc.Input(
        id = 'input1',
        type = 'range',min = 0,max=100,value=50,step=1
    ),
    html.Label('Speed',style={'fontWeight':'bold','fontSize':'20px'}),
    html.Div(id='output_for_speed'),
    dcc.Input(
        type = 'range',
        id = 'input2',min=0,max=2,value=1,step=1
    ),
    dcc.Button('Generate Array' , id = 'generate_array',n_clicks = 0,style ={'marginRight':'10px','backgroundColor':'blue','color':'white'}
    ),
    html.Div(id='buttonclick1'),
    dcc.Button('Start', id='start',n_clicks=0,style ={'marginRight':'10px','backgroundColor':'Green','color':'white'}
    ),
    dcc.Button('Reset', id='reset',n_clicks=0,style ={'marginRight':'10px','backgroundColor':'red','color':'white'}
    ),
    html.H1(['Visualization Area']),
    html.Div(children=[
        dcc.Graph(
            id='visualisation'
        )
    ],style={'height':'400px','border':'2px solid gray','borderRadius':'10px'}),
],
    style = {
        'width':"80%",
        'margin':'0 auto',
        'padding':'20px'
    }
)
## updating the size slider value
@app.callback(
    Output('output_for_size','children'),
    Input('input1','value')
)
def update_output(value):
    return value

## updating the speed slider value
@app.callback(
    Output('output_for_speed','children'),
    Input('input2','value')
)
def update_output(value):
    return value

## Updating the graph bars with array element value as size of bar
@app.callback(
    Output('visualisation','figure'),
    Input('generate_array','n_clicks'),
    State('input1','value')
)
def update_graph(n_clicks,size):
    size = int(size)
    array = random_array(size)
    figure = go.Figure()
    figure.add_trace(
        go.Bar(
            x=list(range(size)),
            y=array
        )
    )
    return figure
if __name__ =='__main__':
    app.run(debug=True)