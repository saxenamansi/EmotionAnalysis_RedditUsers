from dash import Dash, dcc, html
import dash_cytoscape as cyto
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import ast
import json

app = Dash(__name__)

# Load the converted probabilities from the JSON file
with open("emotion_lifecycle_probabilities.json", 'r') as file:
    loaded_probabilities = json.load(file)

# Convert keys (strings) back to tuples
transition_probabilities = {tuple(ast.literal_eval(key)): value for key, value in loaded_probabilities.items()}

# Normalize probabilities
# total_prob = sum(transition_probabilities.values())
# normalized_probabilities = {key: value / total_prob for key, value in transition_probabilities.items()}

# Extract distinct probabilities
distinct_probabilities = set(transition_probabilities.values())

# Create a colormap
cmap = plt.get_cmap("tab10")

# Map distinct probabilities to colors
probability_colors = {prob: to_hex(cmap(i)) for i, prob in enumerate(distinct_probabilities)}

# Create nodes and edges for Dash Cytoscape
nodes = [{"data": {"id": node}} for node in set([node for edge in transition_probabilities.keys() for node in edge])]

# Assign colors to edges based on probability
edges = [
    {
        "data": {"source": source, "target": target, "weight": weight},
        "style": {
            "line-color": probability_colors[weight],
            "target-arrow-color": '#black',
            "target-arrow-shape": 'triangle',
            "target-arrow-fill": 'filled',
            "arrow-scale": 2
        }
    } for (source, target), weight in transition_probabilities.items()
]

# Specify the nodes you want to customize
customized_nodes = {'admiration', 'love', 'joy', 'disappointment'}  # Replace with your node IDs

# Create nodes for Dash Cytoscape with customized text alignment
nodes = [
    {
        "data": {"id": node},
        "style": {
            "content": 'data(id)',
            "background-color": '#6FB1FC',
            "font-size": '30px',
            "text-halign": 'left' if node in customized_nodes else 'right',  # Change the alignment as needed
            "text-valign": 'bottom' if node in customized_nodes else 'top'  # Change the alignment as needed
        }
    } for node in set([node for edge in transition_probabilities.keys() for node in edge])
]



# Create Dash app
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-graph',
        elements=nodes + edges,
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '1000px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'content': 'data(id)',
                    'background-color': '#6FB1FC',
                    'font-size': '30px'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': 'data(style.line-color)',
                    'target-arrow-color': '#gray',  # Change this to black
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier'  # This will enable arrows for all edges
                }
            },
            {
                'selector': 'edge[target != source]',  # Exclude self-loops
                'style': {
                    'target-arrow-shape': 'triangle',
                    'target-arrow-fill': 'filled',
                    'arrow-scale': 2
                }
            }
        ]
    )
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=8890)
