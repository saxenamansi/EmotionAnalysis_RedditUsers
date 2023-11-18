from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

filtered_list = [('admiration', 'approval', ['good', 'best']),
 ('admiration', 'desire', ['good']),
 ('admiration', 'gratitude', ['appreciated']),
 ('admiration', 'love', ['best']),
 ('admiration', 'optimism', ['best']),
 ('admiration', 'surprise', ['appreciated']),
 ('anger', 'annoyance', ['stupid', 'fucking', 'shit', 'hate']),
 ('annoyance', 'disapproval', ['hate', 'cant']),
 ('approval', 'gratitude', ['welcome']),
 ('caring', 'desire', ['please', 'help']),
 ('caring', 'gratitude', ['help']),
 ('caring', 'nervousness', ['help']),
 ('caring', 'optimism', ['help']),
 ('curiosity', 'surprise', ['wondering']),
 ('desire', 'gratitude', ['help', 'would']),
 ('desire', 'nervousness', ['really', 'help']),
 ('disappointment', 'disapproval', ['dont', 'like', 'nt', 'cant']),
 ('disappointment', 'love', ['like']),
 ('embarrassment', 'nervousness', ['really']),
 ('gratitude', 'nervousness', ['thanks', 'help']),
 ('gratitude', 'optimism', ['help']),
 ('gratitude', 'remorse', ['would']),
 ('gratitude', 'surprise', ['appreciated']),
 ('love', 'nervousness', ['really'])]

# Convert filtered_list into Cytoscape elements
elements = []
for relationship in filtered_list:
    elements.append({'data': {'id': relationship[0], 'label': relationship[0], 'type': 'emotion'}})
    elements.append({'data': {'id': relationship[1], 'label': relationship[1], 'type': 'emotion'}})
    for word in relationship[2]:
        elements.append({'data': {'id': word, 'label': word, 'type': 'word'}})
        elements.append({'data': {'source': relationship[0], 'target': word}})
        elements.append({'data': {'source': relationship[1], 'target': word}})

# Define node style based on type
style = [
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'text-valign': 'center',
            'text-halign': 'center',
            'font-size': '25px'
        }
    },
    {
        'selector': 'node[type = "emotion"]',
        'style': {
            'background-color': 'red'  # Color for emotions
        }
    },
    {
        'selector': 'node[type = "word"]',
        'style': {
            'background-color': 'lightgreen',  # Color for words
            'font-size': '20px'
        }
    }
]

app.layout = html.Div([
    html.P("Visualising emotions:"),
    cyto.Cytoscape(
        id='network-graphs-x-cytoscape',
        elements=elements,
        layout={'name': 'breadthfirst'},
        style={'width': '1400px', 'height': '800px'},
        stylesheet=style
    )
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8889)