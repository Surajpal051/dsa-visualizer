from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div(children=[
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
    dcc.Input(
        id = 'input1',
        type = 'range',
    ),
    html.Label('Speed',style={'fontWeight':'bold','fontSize':'20px'}),
    dcc.Input(
        type = 'range',
        id = 'input2'
    ),
    dcc.Button('Generate Array' , id = 'generate array',style ={'marginRight':'10px','backgroundColor':'blue','color':'white'}
    ),
    dcc.Button('Start', id='start',style ={'marginRight':'10px','backgroundColor':'Green','color':'white'}
    ),
    dcc.Button('Reset', id='reset',style ={'marginRight':'10px','backgroundColor':'red','color':'white'}
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

if __name__ =='__main__':
    app.run(debug=True)