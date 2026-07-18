from dash import Dash, html, dcc,Input,Output,State
from utils.randomarray import random_array
app = Dash(__name__)

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
    html.Div(style={'height':'400px','border':'2px solid gray','borderRadius':'10px'}),
],
    style = {
        'width':"80%",
        'margin':'0 auto',
        'padding':'20px'
    }
)

@app.callback(
    Output('output_for_size','children'),
    Input('input1','value')
)
def update_output(value):
    return value
@app.callback(
    Output('output_for_speed','children'),
    Input('input2','value')
)
def update_output(value):
    return value
@app.callback(
    Output('buttonclick1','children'),
    Input('generate_array','n_clicks'),
    State('input1','value')
)

def button_click(n_clicks,size):
    if n_clicks > 0 :
        size = int(size)
        array = random_array(size)
        print(array)

if __name__ =='__main__':
    app.run(debug=True)